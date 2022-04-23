# Update below the LANGUAGE as needed from ['hindi', 'marathi', 'telugu', 'gujarati']
LANGUAGE="telugu"
NAME="${LANGUAGE}_XLSum_v2.0"

echo $LANGUAGE
echo $NAME

cd ./xlsum/
mkdir $NAME/

# In case your tar.bz2 file is somewhere else, Add the path_of_your_downloaded_file before the .tar.bz2 file name below
tar -xf "${NAME}.tar.bz2" -C ./$NAME/

# optional
rm "${NAME}.tar.bz2"

cd ./$NAME/
cat "${LANGUAGE}_train.jsonl" "${LANGUAGE}_val.jsonl" "${LANGUAGE}_test.jsonl" > "./${LANGUAGE}_total.jsonl"

# optional
rm "${LANGUAGE}_train.jsonl" "${LANGUAGE}_val.jsonl" "${LANGUAGE}_test.jsonl"
