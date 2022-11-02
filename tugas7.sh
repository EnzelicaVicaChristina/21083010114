#!?bin?bash

# Mendeklarasikan fungsi
function panjang() {
        echo "Masukkan Panjang : "
        read panjang
}
function lebar() {
        echo "Masukkan Lebar : "
        read lebar
}
function luas() {
        let luas=$panjang*$lebar
        echo "Luas Persegi : "
        echo "$luas"
}

# Memanggil fungsi
panjang
printf "\n"
lebar
printf "\n"
luas
