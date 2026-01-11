def copy_binary(src, dst):
    with open(src, 'rb') as f:
        data = f.read()

    with open(dst, 'wb') as f:
        f.write(data)

copy_binary('Stitch.svg', 'Stitch1.svg')
