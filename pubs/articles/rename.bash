for file in `ls`; do
    mv $file ${file//-/_}
done
