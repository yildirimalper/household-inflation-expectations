# Convert RGB to HEX function
def rgb_to_hex(rgb):
    """Convert an RGB tuple (R, G, B) to HEX format."""
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

# TCMB Official Colors (RGB & HEX)
COLOR_PALETTE = {
    "tcmb_red": rgb_to_hex((213, 0, 50)),
    "tcmb_lacivert": rgb_to_hex((24, 49, 68)),
    "tcmb_bej": rgb_to_hex((212, 190, 155)),
    "tcmb_mavi": rgb_to_hex((94, 140, 198)),
    "tcmb_sari": rgb_to_hex((249, 194, 19)),
    "tcmb_mor": rgb_to_hex((181, 148, 182)),
    "tcmb_yesil": rgb_to_hex((19, 117, 71)),
    "tcmb_ayesil": rgb_to_hex((57, 181, 178)),
    "tcmb_gri": rgb_to_hex((102, 102, 102)),
    "tcmb_pembe": rgb_to_hex((255, 204, 201))
}
