{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "58771a71-8864-4a8a-b24b-3dc6d3829f55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Plaintext asli  : sabbe satta bhavantu sukhiatta\n",
      "Ciphertext      : 242e533195077fe59afed11ee5caf06817f80f855cfe28b70e985f509c7bc1df\n",
      "Hasil deskripsi : sabbe satta bhavantu sukhiatta\n"
     ]
    }
   ],
   "source": [
    "from Crypto.Cipher import AES\n",
    "from Crypto.Util.Padding import pad, unpad\n",
    "\n",
    "plaintext = \"sabbe satta bhavantu sukhiatta\"\n",
    "key = b'Brianputralendeb'  # Panjang 16 byte, sesuai AES-128\n",
    "\n",
    "data = plaintext.encode('utf-8')\n",
    "data_padded = pad(data, AES.block_size)\n",
    "cipher = AES.new(key, AES.MODE_ECB)\n",
    "ciphertext = cipher.encrypt(data_padded)\n",
    "\n",
    "\n",
    "cipher_dec = AES.new(key, AES.MODE_ECB)\n",
    "decrypted = unpad(cipher_dec.decrypt(ciphertext), AES.block_size)\n",
    "\n",
    "\n",
    "print(\"Plaintext asli  :\", plaintext)\n",
    "print(\"Ciphertext      :\", ciphertext.hex())\n",
    "print(\"Hasil deskripsi :\", decrypted.decode('utf-8'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f9ac2103-54a6-4fa8-8a2d-0986b0de9e33",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f2ed503a-5d18-4b4d-9431-6b75dffaf2b5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
