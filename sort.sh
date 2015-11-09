for each in *.mkv
do
  date=$(date +%Y-%d-%m -r "$each");
  _DATES+=($date);
  FILES+=($each);
done

DATES=$(printf "%s\n" "${_DATES[@]}" | sort -u);
for date in ${DATES[@]}; do
  if [ ! -d "$date" ]; then
    mkdir "$date"
  fi
done

for i in  ${FILES[@]}; do
  dest=$(date +%Y-%d-%m -r "$i")
  mv $i $dest/$i
done
