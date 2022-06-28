# By Ezz

import base64 as base

print("\n[1] Encoding With base85")
print("[2] Encoding With base64")
print("[3] Encoding With base32")
print("[4] Encoding With base16")
print("[5] Encoding With ASCII85") # ACSII Means: American Standard Information Interchange

Base = str(input("\nWhat Encode Type Do You Want: ")).lower().strip()


if Base == "base85" or Base.endswith("85") or Base == "1":

    base85_encodeing = str(
        input("\nBase85, Enter a Word To Encode It: ")).lower().strip()

    b = base85_encodeing.encode("UTF-8")
    e = base.b85encode(b)

    print(f"\nBase85 Encoded: {e}")


elif Base == "base64" or Base.endswith("64") or Base == "2":

    base64_encodeing = str(
        input("\nBase64, Enter a Word To Encode It: ")).lower().strip()

    b1 = base64_encodeing.encode("UTF-8")
    b2 = base.b64encode(b1)

    print(f"\nBase64 Encoded: {b2}")


elif Base == "base32" or Base.endswith("32") or Base == "3":

    base32_encodeing = str(
        input("\nBase32, Enter a Word To Encode It: ")).lower().strip()

    b1 = base32_encodeing.encode("UTF-8")
    b2 = base.b32encode(b1)

    print(f"\nBase32 Encoded: {b2}")


elif Base == "base16" or Base.endswith("16") or Base == "4":

    base16_encodeing = str(
        input("\nBase16, Enter a Word To Encode It: ")).lower().strip()

    b1 = base16_encodeing.encode("UTF-8")
    b2 = base.b16encode(b1)

    print(f"\nBase16 Encoded: {b2}")


elif Base == "ascii85" or Base.startswith("a") or Base == "5":

    ASCII85_encodeing = str(
        input("\nASCII85, Enter a Word To Encode It: ")).lower().strip()

    b1 = ASCII85_encodeing.encode("UTF-8")
    b2 = base.a85encode(b1)

    print(f"\nASCII85 Encoded: {b2}")
