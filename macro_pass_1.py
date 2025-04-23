mnt = {}
mdt = []
ala_table = {}

in_macro = False
macro_name = ""
mdt_index = 0

with open("source.asm") as file:
    for line in file:
        stripped = line.strip()
        if stripped == "MACRO":
            in_macro = True
            continue
        elif stripped == "MEND":
            in_macro = False
            mdt.append("MEND")
            mnt[macro_name] = mdt_index
            mdt_index = len(mdt)
            continue

        if in_macro:
            tokens = stripped.split()
            if not macro_name:
                macro_name = tokens[0]
                params = tokens[1:] if len(tokens) > 1 else []
                ala_table[macro_name] = params
            mdt.append(stripped)
        else:
            macro_name = ""

print("MNT (Macro Name Table):")
for name, index in mnt.items():
    print(f"{name} -> MDT index {index}")

print("\nMDT (Macro Definition Table):")
for i, line in enumerate(mdt):
    print(f"{i}: {line}")

print("\nALA (Argument List Array):")
for name, args in ala_table.items():
    print(f"{name}: {args}")
