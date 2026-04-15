import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.UUID;

/**
 * Demuestra el bug de endianness en la serialización/deserialización de UUIDs.
 *
 * El bug ocurre cuando:
 *   1. Un UUID se convierte a bytes[] en orden LITTLE ENDIAN (p.ej. desde .NET, MySQL, etc.)
 *   2. Esos mismos bytes se usan para reconstruir el UUID interpretándolos como BIG ENDIAN
 *
 * Resultado: el UUID reconstruido es distinto al original.
 */
public class UuidEndianBug {

    public static void main(String[] args) {

        // --- Paso 1: Generar un UUID ---
        UUID original = UUID.randomUUID();
        System.out.println("=== UUID Endianness Bug Demo ===");
        System.out.println();
        System.out.println("[1] UUID original:              " + original);

        // --- Paso 2: Convertir a bytes[] en LITTLE ENDIAN ---
        byte[] leBytesGood = toByteArrayLittleEndian(original);
        System.out.print("[2] Bytes en little endian:     ");
        printBytes(leBytesGood);

        // --- Paso 3 (correcto, para referencia): bytes en BIG ENDIAN ---
        byte[] beBytes = toByteArrayBigEndian(original);
        System.out.print("    Bytes en big endian (ref):  ");
        printBytes(beBytes);

        System.out.println();

        // --- Paso 4: EL BUG — reconstruir el UUID desde bytes little endian
        //             pero interpretándolos como big endian ---
        UUID buggedUuid = fromByteArrayAsBigEndian(leBytesGood);
        System.out.println("[3] UUID reconstruido (con bug): " + buggedUuid);
        System.out.println();

        // --- Verificación ---
        System.out.println("¿UUID original == UUID reconstruido? " + original.equals(buggedUuid));
        System.out.println();
        System.out.println("CONCLUSION: Los bytes se guardaron en little endian pero se leyeron");
        System.out.println("            como big endian, produciendo un UUID completamente distinto.");
    }

    /**
     * Serializa un UUID a 16 bytes en orden LITTLE ENDIAN.
     * Así lo haría, por ejemplo, .NET (Guid.ToByteArray()) o algunos drivers de MySQL.
     */
    static byte[] toByteArrayLittleEndian(UUID uuid) {
        ByteBuffer buf = ByteBuffer.allocate(16);
        buf.order(ByteOrder.LITTLE_ENDIAN);
        buf.putLong(uuid.getMostSignificantBits());
        buf.putLong(uuid.getLeastSignificantBits());
        return buf.array();
    }

    /**
     * Serializa un UUID a 16 bytes en orden BIG ENDIAN (el estándar RFC 4122).
     * Así lo hace Java por defecto con ByteBuffer.
     */
    static byte[] toByteArrayBigEndian(UUID uuid) {
        ByteBuffer buf = ByteBuffer.allocate(16);
        buf.order(ByteOrder.BIG_ENDIAN);
        buf.putLong(uuid.getMostSignificantBits());
        buf.putLong(uuid.getLeastSignificantBits());
        return buf.array();
    }

    /**
     * EL BUG: toma bytes que están en little endian y los interpreta como big endian.
     * Esto ocurre cuando se usa ByteBuffer.wrap(bytes) sin setear el order correcto,
     * ya que el default de ByteBuffer es BIG_ENDIAN.
     */
    static UUID fromByteArrayAsBigEndian(byte[] bytes) {
        ByteBuffer buf = ByteBuffer.wrap(bytes);
        // BUG: no se especifica ByteOrder.LITTLE_ENDIAN, por lo que usa BIG_ENDIAN por defecto
        buf.order(ByteOrder.BIG_ENDIAN);
        long msb = buf.getLong();
        long lsb = buf.getLong();
        return new UUID(msb, lsb);
    }

    static void printBytes(byte[] bytes) {
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < bytes.length; i++) {
            sb.append(String.format("0x%02X", bytes[i]));
            if (i < bytes.length - 1) sb.append(", ");
        }
        sb.append("]");
        System.out.println(sb);
    }
}
