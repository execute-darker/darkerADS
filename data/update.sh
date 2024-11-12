#!/bin/bash
DIR="./data/temp"
list="
https://gp.adrules.top/adblock_plus.txt
https://gp.adrules.top/dns.txt  
https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt
https://adguardteam.github.io/HostlistsRegistry/assets/filter_2.txt
https://adguardteam.github.io/HostlistsRegistry/assets/filter_29.txt
https://adguardteam.github.io/HostlistsRegistry/assets/filter_21.txt
https://adguardteam.github.io/HostlistsRegistry/assets/filter_24.txt
https://adguardteam.github.io/HostlistsRegistry/assets/filter_38.txt
https://mirror.ghproxy.com/raw.githubusercontent.com/8680/GOODBYEADS/master/data/rules/dns.txt
https://mirror.ghproxy.com/raw.githubusercontent.com/8680/GOODBYEADS/master/data/rules/allow.txt
https://mirror.ghproxy.com/raw.githubusercontent.com/8680/GOODBYEADS/master/data/rules/adblock.txt
"

mkdir "$DIR"
for i in $list; do
    curl -vLk $i -o "$DIR/$(date +%s).txt"
done
for i in $(ls -1 "$DIR"); do
    cat "$DIR/$i" >>"$DIR/all.txt"
    rm -rf "$DIR/$i"
done
sort -u "$DIR/all.txt" >"$DIR/temp.txt"
mv "$DIR/temp.txt" "./adblock.txt"
rm -rf "$DIR"
