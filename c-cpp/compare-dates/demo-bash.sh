#! /bin/bash

echo "Auto generate create_files.sh & run_all.sh"

ROOT_FS=$(dirname "${BASH_SOURCE}")

cat > $ROOT_FS/create_files.sh << EOF
echo -n "this is f1" > $ROOT_FS/f1.txt
echo -e "this is F1\n" > $ROOT_FS/f2.txt
EOF

chmod +x $ROOT_FS/create_files.sh

cat > $ROOT_FS/run_all.sh << EOF1
$ROOT_FS/create_files.sh
diff -i $ROOT_FS/f1.txt $ROOT_FS/f2.txt
EOF1

chmod +x $ROOT_FS/run_all.sh

read -n1 -r -p "Press q to quit, or any other key to invoke run_all.sh scripts..." key

if [ "$key" = 'q' ]; then
    exit
else
    $ROOT_FS/run_all.sh
fi

read -n1 -r -p "Press q to quit, or any other key to delete newly created text files..." key

if [ "$key" = 'q' ]; then
    exit
else
    # Anything else pressed, do whatever else.
    # echo [$key] not empty

    CMD="rm -f f1.txt f2.txt"
    echo $CMD > $ROOT_FS/delete.txt
    $CMD
fi
