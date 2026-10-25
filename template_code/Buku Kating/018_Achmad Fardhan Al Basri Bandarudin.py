from utils import (
    setup_buku_kating_page,
    streamlit_menu,
    display_images_with_data,
)

setup_buku_kating_page()
menu = streamlit_menu()

# ============================================================
# MENU CONTENT
# ============================================================
if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=12QdXjuDnQDgFjZ53SQuKa14r1KlfZdtC",
        "https://drive.google.com/uc?export=view&id=1dCRWi5V03bDmaN8EXzTquEh56RbmzWH5",
        "https://drive.google.com/uc?export=view&id=1Nl37phlxmCYNGC8fQiEWGBngxmdTYWrS",
        "https://drive.google.com/uc?export=view&id=1-RHonktea6ug0hMHWJb075mq8lUfSxVo",
        "https://drive.google.com/uc?export=view&id=1tPhSsXlKDmI0HV1lXhVVXZ3pj-SlX6-1",
        "https://drive.google.com/uc?export=view&id=1J_tlUQwAwRqlkmQ1ctjO6VxpS9syNjG6",
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abangnya seruu, dlu pernah jadi kadiv op pas natal SD25 bisa diajak serius dan bercanda.", "pesan": "Semangat dan suksek selalu bangg!!"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jendral", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Kesekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya seru bisa diajak bercanda dan bisa diajak bicara serius.", "pesan": "Sukses selalu serta semangat dalam melaksanakan tugas!"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya murah senyum.", "pesan": "Sukses selalu kak dan semangat!"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya sof spoken, lucuu.", "pesan": "Sukses selalu dan semangat bang!!"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik, murah senyum, dan suka duit.", "pesan": "Sukses selalu dan semangat kakk!!"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya seru, lucuu, baikk.", "pesan": "Sukses selalu dan semangat kakkk!!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="kesekjenan")

elif menu == "Baleg":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1nb6wQCMKYJ-qpm_JJX5mf3ZNLK-J_H3i",
                   "https://drive.google.com/uc?export=view&id=17OL5MYhd-mPGuqd3MQUn-GEt3F0BzWdV",
                   "https://drive.google.com/uc?export=view&id=1PwKjv3GE4YpyIHMxbgZuSV0X6DOnCKPm",
                   "https://drive.google.com/uc?export=view&id=13r76KMeRBGdgw_T1BS1qSyZop0qHoUir",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1asiSAi8307nYlUj6NELCI7r3VXVlVE3q",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1kLwtXjx2olEgmOaEKgusg7kVCJUBDHFe",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1IagjaSmKoMlNQuKstWP2TbyQVig0eUZe",
                   "https://drive.google.com/uc?export=view&id=1IVbitzGVgyhbI1W3YRlHSdMaHfyqDmWG",
                   "https://drive.google.com/uc?export=view&id=1WFD00bxXLtyJKy2gBjM1N_Hsd38ainaa",
                   "https://drive.google.com/uc?export=view&id=1IlzmNGNYQx6UilONk2kXu0NQqyXjeNsv",
    ]
    data_list = [
        {"nama": "Anggota Baleg", "jabatan": "Ketua Badan Legislatif", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="baleg")

elif menu == "Senator":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1adDzBL83GRxrkpCHbabR-KGkHvdDaDLw",
                   "https://drive.google.com/uc?export=view&id=1h6knY8DO-nKuqMLUGbB0WiP_vZ2hnXxl",
                   "https://drive.google.com/uc?export=view&id=1OzMDgEK9aGkBknqyE7YTUvZisSXt9vvX",
                   "https://drive.google.com/uc?export=view&id=1sT6F4idooVcQzZEOlpZFD5uZhVlTs4dQ",
                   "https://drive.google.com/uc?export=view&id=1yYdbKWsiGJwdy2BLhuUw3Knv8nYBUCup",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1uUf8cobIcp275cg1nhdsgv4u8028adTF",
                   "https://drive.google.com/uc?export=view&id=1dpucSmlYuZfVW9W3tPnpmAxQsctbXr63",
                   "https://drive.google.com/uc?export=view&id=13tfR7Wt7bwXk6pAv6KzyRxoIniUn2xbr",
                   "https://drive.google.com/uc?export=view&id=1kdFTZEnPYkuNpJG0jHDK1qz9ImbP4LE8",
    ]
    data_list = [{"nama": "Anggota Senator", "jabatan": "Senator Mahasiswa", "nim": "122450022", "umur": "21", "asal": "Jakarta", "alamat": "Sukarame", "hobbi": "Debat", "sosmed": "@senator", "kesan": "Informatif", "pesan": "Terus berkarya!"}] * 11
    display_images_with_data(gambar_urls, data_list, key="senator")

elif menu == "Departemen PSDA":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1Wuc4L6sgBoo0_bEfODDm4qnmhV0lb5Fs",
                   "https://drive.google.com/uc?export=view&id=1mYHpz8j3-LdffghK3--meBlWQV6S6TRE",
                   "https://drive.google.com/uc?export=view&id=1lhv5Fzb2y7vN6dKi3-iFs2kP29Opl_Wa",
                   "https://drive.google.com/uc?export=view&id=1ord9VbP1G8yKkezIjNab8CBwUPEV_q12",
                   "https://drive.google.com/uc?export=view&id=1mMekmzXyU1mld6BgK4yJVSBBfdp4LOJq",
                   "https://drive.google.com/uc?export=view&id=1rjP2j9ScK6YgzGP1FsTQJcNX5tiJwgiX",
                   "https://drive.google.com/uc?export=view&id=1HAql4KGgPOKK_NAKQr-MDrERmW_2CXre",
                   "https://drive.google.com/uc?export=view&id=19R7Y9-gHOeLnSQLBkM2KvmUhlF7UXgYm",
                   "https://drive.google.com/uc?export=view&id=1Ab96qg09_6NUt8LGb8yme7WSErzvvhEh",
                   "https://drive.google.com/uc?export=view&id=1Htn6O5u6FeCM-EgAwzdYhl0hwGcIwr2q",
                   "https://drive.google.com/uc?export=view&id=1T3En8p8NqynR7wSEqNRTtn2JVUjlLLRw",
                   "https://drive.google.com/uc?export=view&id=1ULsT6Pk7G7dSbUbjx3GFDpTRuA_uOglf",
                   "https://drive.google.com/uc?export=view&id=1WJatEYATBbA-ex6gPJKNzE-6_fHzTnKI",
                   "https://drive.google.com/uc?export=view&id=1_J8cADzoEhS_gwj9OfK--v0GtK1b8Xmn",
                   "https://drive.google.com/uc?export=view&id=1nDp-XlUNqD0CR5bHBR-9soFX16zo1nmT",
                   "https://drive.google.com/uc?export=view&id=1BhoiSznhDKNgzQPiGKd8ycLRQqWwOM6p",
                   "https://drive.google.com/uc?export=view&id=1OXFzj9MDHDtUtI_T-04-qy7uf5zsaO8w",
    ]
    data_list = [
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="psda")

elif menu == "Departemen MIKFES":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1Vrf6tfghe4NB6LkTN8Oknosvx-tvjIuT",
                   "https://drive.google.com/uc?export=view&id=1DJHzP85moU2DdSX4CxJGm-_-F41UjGNy",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy",
                   "https://drive.google.com/uc?export=view&id=19TTnEGSUEpbkRYRqOHKYryECCpjv8C4R",
                   "https://drive.google.com/uc?export=view&id=1yOoxvdC9Gt64-rwPCIGI7Ewa2cNO0By3",
                   "https://drive.google.com/uc?export=view&id=1UhJh2xq3RUjmqHllYVMonwgll5fWdK-H",
                   "https://drive.google.com/uc?export=view&id=1RT0VsPQObAZZoP-JNpek2y7ebUxtD4ru",
                   "https://drive.google.com/uc?export=view&id=1dsdC6LlV7SHIZcD6_hFts6VZtBamXW1w",
                   "https://drive.google.com/uc?export=view&id=1DvKA-VfwJO5JL-evbEIcPqAyGl4d2J8d",
                   "https://drive.google.com/uc?export=view&id=1r4HNsPcYjhAg4qakI7gCZbEiyvZ3Q2KH",
                   "https://drive.google.com/uc?export=view&id=1ZXVJfjxABm470NG57wIeuO8ffBHkq-AY",
                   "https://drive.google.com/uc?export=view&id=1c82ZZAFTaTMTO_BuF5xBZabozz5Kpn-P",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1jxM3Zx3NsXFshrSiumapbCEDaDhc1OJi",
                   "https://drive.google.com/uc?export=view&id=1JlZ1I2w6r4cwtLnN1Lhz0A70vW6tBf3p",
                   "https://drive.google.com/uc?export=view&id=1XZ24oWA_GIp8ugfyixhyooo25sy8CSB1",
                   "https://drive.google.com/uc?export=view&id=1g26jRfNBn8JKtfyZ1MSzFtm3MGiTdnhb",
                   "https://drive.google.com/uc?export=view&id=1nd6kcxPIYZos6NGcGxPTYA2-GJiV6reQ",
                   "https://drive.google.com/uc?export=view&id=14SmXrXQ-mBZ7dBBBtjJRp6_PpGBuwI_X",
                   "https://drive.google.com/uc?export=view&id=1LTfRoN1EDCeTC9SdaSF_XVqZM6Y1rBMZ",
                   "https://drive.google.com/uc?export=view&id=1Dt2btj9-PSXxtbddvVMJCDaRXpo14ZoI",
                   "https://drive.google.com/uc?export=view&id=18CBehY0eqQRgc0Y1ETHMpzyo8cFdgPUE",
    ]
    data_list = [
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="mikfes")

elif menu == "Departemen Eksternal":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1u0GPQcg6pHKddidEpCW03MXJf09nWlIS",
                   "https://drive.google.com/uc?export=view&id=1JTz0JQx0o9-41SIRGD65asvBT12cblY4",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=19rM4QJg_4tsWzJQVcz4iQGMy3TXh2-yu",
                   "https://drive.google.com/uc?export=view&id=1dIbxHxXQppoA-M3k5EepeIBTDQUVsy3d",
                   "https://drive.google.com/uc?export=view&id=1ZnDz5dmr5l393QuVk5n_jTLGG5Vz9npw",
                   "https://drive.google.com/uc?export=view&id=1NmEcnANricdiLQHQpOMmpoTRC0Hye78q",
                   "https://drive.google.com/uc?export=view&id=1xjrIXgMNPoQ2HWIy999JwbwxAo7082Tv",
                   "https://drive.google.com/uc?export=view&id=1_naA2Pr1kaARtrUhbugRY-kCZ2YJK8au",
                   "https://drive.google.com/uc?export=view&id=1aW5YaTpcIe2qXV7T7tcHXWcJl3vWjq58",
                   "https://drive.google.com/uc?export=view&id=1f1lZjkYB4GiIoHMD_9Z_4GHE5QFK-2kN",
                   "https://drive.google.com/uc?export=view&id=1B2zO2sAjI6f1wfg6j4laPwVWBGaBcKPn",
                   "https://drive.google.com/uc?export=view&id=1dzpXZ3fCjKBS1W2zAoCvIZ0_Au2xQOQR",
                   "https://drive.google.com/uc?export=view&id=1R_vevwV9Cc9w48X4QFc01NdkzzAULZM9",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1QM_o_q09j0JHvWvTY_vTxlDQAdwrqEOP",
                   "https://drive.google.com/uc?export=view&id=1XIbGvb-weBGgRegGDou624O_JMaSEMxV",
                   "https://drive.google.com/uc?export=view&id=1NI01CC_jV1yL6PEoK0TNs187fAWD7oJD",
                   "https://drive.google.com/uc?export=view&id=1Cirzwsa96DiGo8VzurOpFQ21X8yzyDAF",
                   "https://drive.google.com/uc?export=view&id=1XhM8mEeL6RGY90UOEVNV2HUa0w81muwm",
                   "https://drive.google.com/uc?export=view&id=1ZoMYZhC_1_jndLI6bYX7PjKDj1FTSYum",
                   "https://drive.google.com/uc?export=view&id=1cbKV3XfEjp40oQfndBzi438W3I79ymLP",
    ]
    data_list = [{"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="eksternal")

elif menu == "Departemen Internal":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1Qg9iT4ppQ45YFIjoEoIxQ_g6MTbWnynB",
                   "https://drive.google.com/uc?export=view&id=1Y7MDaZXYo5vgq7ys0OfAPb_gnc1VyAhx",
                   "https://drive.google.com/uc?export=view&id=1SaRStJOtsNOuFmJh4KugmkB4USQi8CEq",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bg farhan
                   "https://drive.google.com/uc?export=view&id=18crJAyEqY6DyIqbpZghKkkfWQQoxBbff",
                   "https://drive.google.com/uc?export=view&id=1BsDaOvqb1cUerICtSyA34NepJFIiyzPx",
                   "https://drive.google.com/uc?export=view&id=1z2zPCwICtKXmjKXPrkHz_36WJ13VSgSk", 
                   "https://drive.google.com/uc?export=view&id=1c0M4qugAMtMNI_582UFtOFPhXZe24Znt",
                   "https://drive.google.com/uc?export=view&id=1bJ_IJg4uEXqZceG0XwIt_QPvPKZReylK",
                   "https://drive.google.com/uc?export=view&id=1q93vvZb2ymsxed7qxBO5VYLdmS7myBU5", 
                   "https://drive.google.com/uc?export=view&id=1sDRImohzil7wDem8OWoo-UEeLUkeHLSN",
                   "https://drive.google.com/uc?export=view&id=1urUksXckK29uycn-PYEr5J3tm0wmV6R7",
                   "https://drive.google.com/uc?export=view&id=1o_wExnoejzGXjp6gRfN1pINRVpVS6by8",
                   "https://drive.google.com/uc?export=view&id=1GUdEDsFa2vtasR_pqN3jfvAKbl0BNQsz",
                   "https://drive.google.com/uc?export=view&id=1YTkJwCJ33mkzrI0ZWvZCuTiadQQNesHx",
                   "https://drive.google.com/uc?export=view&id=1sbgqsVlY3R_GQi_9S5Rs-fyFgCL6_0mv",
                  
    ]
    data_list = [
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="internal")

elif menu == "Departemen SSD":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1e2lyEW3Tt1s_reEotgt6YgXt6QgoxFNo",
                   "https://drive.google.com/uc?export=view&id=1nvNY6Q4-bvt4oZdnnhEjGoPt3xr2baeI",
                   "https://drive.google.com/uc?export=view&id=1DFI7WURFKOXwQ1LQUR3Eu9bGW3tEVE-O",
                   "https://drive.google.com/uc?export=view&id=1n2VOosrTtoArBMyCGoDmMecLGnGnTo6W",
                   "https://drive.google.com/uc?export=view&id=1KzdXaRGL_f_W-YQcPVKeLR1GfFhAv4zQ",
                   "https://drive.google.com/uc?export=view&id=1aRXo2dZIW5Kohof94cwtpQgHCQsT7ubY",
                   "https://drive.google.com/uc?export=view&id=11V7sGDZ4w5Z6bE4TomfZUcnQPl_2fJVf",
                   "https://drive.google.com/uc?export=view&id=1uXIjyfX6Cb9bOFGFdUtcrgdMBn9NCwZF",
                   "https://drive.google.com/uc?export=view&id=1603I5xBQpFHTPm0NMgyoOats53W2WHy1",
                   "https://drive.google.com/uc?export=view&id=1r6_C9O2tuNk1U6adKEs7W8lTTMaywsz-",
                   "https://drive.google.com/uc?export=view&id=1nUDxWI0MmRglG4nvEfuUcw9wcTIX7OoS",
                   "https://drive.google.com/uc?export=view&id=1-Tf7Dh2YmI7FAmz-BnTs48AjryAnRTAW",
                  
    ]
    data_list = [{"nama": "Anggota SSD", "jabatan": "Staf SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"}] * 12
    display_images_with_data(gambar_urls, data_list, key="ssd")

elif menu == "Departemen Medkraf":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1gv3ZHruRvhlqjqB0J12SCNq9VCGXZtHc",
        "https://drive.google.com/uc?export=view&id=1FG-5QwmDV7R5bgK3lRgvC55ozV-T8xEc",
        "https://drive.google.com/uc?export=view&id=1_70DlvPCXP-ieUQZ9xrTGkVm5bi75qiO",
        "https://drive.google.com/uc?export=view&id=1F_fy0dfhNKc-7bsu21cYxT1UDqSKHlc9",
        "https://drive.google.com/uc?export=view&id=1qAVzBUQq_QixAItTOsaFfbZC2KbcOAm2",
        "https://drive.google.com/uc?export=view&id=1q5XbzPqW6KaNjG6XzsXXYFficU-8qKwd",
        "https://drive.google.com/uc?export=view&id=18WVqqF7nxsjJ7c7IxtmDxAJ9gdbWhLJH",
        "https://drive.google.com/uc?export=view&id=1qrAYXB3Owg7DEMd1L7-f4jFaAHSW3Igp",
        "https://drive.google.com/uc?export=view&id=13mDNYZ-qMSJlMYZanFv660qduwh_Ngvr",
        "https://drive.google.com/uc?export=view&id=1nfV7vSieHHKnSPa9pK8wzPmKlEPAXUPM",
        "https://drive.google.com/uc?export=view&id=1SQSauv4w9N0FxOM6b_6MdWskVhONcr4f",
        "https://drive.google.com/uc?export=view&id=1hcCYJ1Hmzrg3xcyMgFrRCivDLnS0L9m3",
        "https://drive.google.com/uc?export=view&id=183prjg4UbgWRI1_0cjfCLjOk_cxZbIDN",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1ggfQxOGhgw7tNjK-t56bkmJARW_tlgSR",
        "https://drive.google.com/uc?export=view&id=1ATCPWdkLwWtCMlz49j7gyuypsD1kHCK9",
        "https://drive.google.com/uc?export=view&id=1PaSfCj8UMMs9Lzyp72SigsCnat0NXNmd",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
    ]
    data_list = [{"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"}] * 18
    display_images_with_data(gambar_urls, data_list, key="medkraf")

elif menu == "Departemen MINBAK":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1rTmyPLmmDxWdvEsGojwQjDQTovodjHXH",
        "https://drive.google.com/uc?export=view&id=1-Ul5mfV_JXU_tk4ewgtPAwNKRjDvcI_O",
        "https://drive.google.com/uc?export=view&id=1koQA-1DFOIst7QmIp8QiqEG_i0uKC6hw",
        "https://drive.google.com/uc?export=view&id=1oBwVTXUj1JzhE1SfY7AJ6HW02kQqm4r9",
        "https://drive.google.com/uc?export=view&id=1S368q3066zNocOivsVIfT3HPMacAOnwU",
        "https://drive.google.com/uc?export=view&id=1HAGEusSLz7Op2kSiqAKU3BSS5nfonb1U",
        "https://drive.google.com/uc?export=view&id=1x4xqU9dtQfgjl_PD_inA2NfDJSl_IJnG",
        "https://drive.google.com/uc?export=view&id=13FW3ZkOoZlrV3z8mmEN71GWzGeDPjnU_",
        "https://drive.google.com/uc?export=view&id=1ELAQDS9dg80CPedaIymlWZh0l5uSefp9",
        "https://drive.google.com/uc?export=view&id=1ezjw-g4sBfWNZuNWvWHfUlKpUs8qgzMG",
        "https://drive.google.com/uc?export=view&id=10dw6LaqrRzuGU9ndHKfU74mW0yxsYRqf",
        "https://drive.google.com/uc?export=view&id=1BDlk31IbbCvMF9wBAneSRfrCItNHpP-J",
        "https://drive.google.com/uc?export=view&id=1dOPlMxo4Ztv6ZAjYS0USlm18DSK6CB7c",
        "https://drive.google.com/uc?export=view&id=16-Va12Or_hc5nfa2s2GXuya756S666Mk",
        "https://drive.google.com/uc?export=view&id=13oe9JWflY4KkHze5eszVV7xJ-4uKfWXF",
    ]
    data_list = [
        {"nama": "Kevin Antonio Junior", "jabatan": "Staf Medkraf", "nim": "123450082", "umur": "20", "asal": "Payakumbuh, Sumatera Barat", "alamat": "Way Huwi", "hobbi": "Musingin TA", "sosmed": "@naylasalsabilaa._", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Gusti Putu Ferazka D.", "jabatan": "Staf Medkraf", "nim": "123450028", "umur": "20", "asal": "Bekasi", "alamat": "Way Huwi", "hobbi": "Berenang", "sosmed": "@donnamaya.p", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Ali Aristo Muthahhari Parisi", "jabatan": "Staf Medkraf", "nim": "123450037", "umur": "20", "asal": "Medan, Jakut, Palembang", "alamat": "Way Huwi", "hobbi": "Buka tutup laptop", "sosmed": "@noerruuu", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Ayu Andriani Parlina Wati", "jabatan": "Staf Medkraf", "nim": "124450050", "umur": "20", "asal": "Bandar Lampung", "alamat": "Way Huwi", "hobbi": "Ballet", "sosmed": "@anshtsyaaql", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Dafa Elpriza", "jabatan": "Staf Medkraf", "nim": "124450104", "umur": "18", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Mancing emosi", "sosmed": "@felisyanbl", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Juwita Sari", "jabatan": "Staf Medkraf", "nim": "124450031", "umur": "18", "asal": "Tangerang Selatan", "alamat": "Ryacudu", "hobbi": "Badminton ama tensor 24", "sosmed": "@muh_razan_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Muhammad Afdal Lutfi", "jabatan": "Staf Medkraf", "nim": "123450087", "umur": "21", "asal": "Karawang", "alamat": "Airan", "hobbi": "Nongkrong depan ruang prodi", "sosmed": "@saniayyllstr", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Salsabila Nazwa Putri", "jabatan": "Staf Medkraf", "nim": "125450019", "umur": "3", "asal": "Jepang", "alamat": "Cafe Kali", "hobbi": "Jalan bareng my love", "sosmed": "@aallishaa.aa", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Muhammad Ridwan", "jabatan": "Staf Medkraf", "nim": "124450091", "umur": "19", "asal": "Jambi", "alamat": "Airan", "hobbi": "Main futsal", "sosmed": "@alya.rmdhnti", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Andra Ilham Bintang", "jabatan": "Staf Medkraf", "nim": "124450097", "umur": "2", "asal": "Sidomulyo", "alamat": "Pemda", "hobbi": "Mengkoding", "sosmed": "@buncaclrssf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Bryan Paskah Telaumbanua", "jabatan": "Staf Medkraf", "nim": "124450043", "umur": "7.137 hari per hari ini", "asal": "Kalimantan Utara", "alamat": "Deket ITERA", "hobbi": "Mancing mania", "sosmed": "@difanyhsa", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Ghiyats Thabularasa Meardhy", "jabatan": "Staf Medkraf", "nim": "124450054", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Main badmin lawan razan", "sosmed": "@nzlhauly_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Indah Julia Mawar Pratiwi", "jabatan": "Staf Medkraf", "nim": "123450041", "umur": "20", "asal": "Lampung tengah", "alamat": "Airan Raya 1", "hobbi": "Membaca, menulis", "sosmed": "@n1tg._", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Jacinda Kesya Alvara", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Muhammad Rafka Fatih Al Ghathfaan", "jabatan": "Staf Medkraf", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Scrolling Fesbuk", "sosmed": "@eddel_0712", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},

    ]
    display_images_with_data(gambar_urls, data_list, key="minbak")
