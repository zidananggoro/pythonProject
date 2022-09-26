def display_greeting():
    print("selamat datang di car sales, here kamu bisa pilih ")
    print("mobil impian mu, dan kami akan memberi tahu harga yang akan di keluarkan")

def display_prompt():
    print("apa yang akan kamu lakukan")
    print("a - memberli mobil")
    print("b - Exit")

def get_user_option():
    display_prompt()
    user_option = input("> ")

    while user_option == "":
        print("kamu pilih opsi yang dipilih")
        display_prompt()
        user_option = input("> ")

    return user_option
def get_car(user_option):
    available_cars = dict()

    available_cars[1] = "honca civic ( baru )"
    available_cars[2] = "pedah ( bekas )"
    available_cars[3] = "dokar ( baru )"
    available_cars[4] = "becak ( baru )"
    available_cars[5] = "tikar ( bekas )"

    if user_option == 'b':
        print("goodbye")
        quit()
    elif user_option == 'a':
        print("")
        print("pilihan yang anda pilih")
        for i in range(len(available_cars)):
            print(f"{i+1}. {available_cars[i+1]}")
        user_car_option = int(input("> "))

        while user_car_option == "":
            print("")
            print("pilihan yang kamu pilih : ")
            for i in range(len(available_cars)):
                print(f"{i+1}. {available_cars[i+1]}")
            user_car_option = int(input("> "))
        return available_cars[user_car_option]
def get_car_price(car_type):
    car_price = 0
    print("")
    print(f"{car_type} mobil bagus")
    print(" mobil sedang tersedia")
    user_car_year = int(input("> "))

    while (2008 >= user_car_year <= 2022):
        print("")
        print("type mobil tesedia")
        user_car_year = int(input("> "))

        if user_car_year >= 2008 and user_car_year <= 2010:
            car_price = 8000
        elif user_car_year >= 20011 and user_car_year <= 2013:
            car_price = 8000
        elif user_car_year >= 2014 and user_car_year <= 2016:
            car_price = 8000
        elif user_car_year >= 2017 and user_car_year <= 2019:
            car_price = 8000
        elif user_car_year >= 2020 and user_car_year <= 2022:
            car_price = 8000

def get_confirmation(price,car_type, user_option):
    print("")
    print(f"luar biasa, silah pilihan anda anda pilih:")
    print(f"\tCar make & model: {car_type}")
    print(f"\tCar price : &{price}")
    print("")
    print("apakan beneran membeli mobil ini? (Y/N)")
    response = input("> ")
    response.lower()

    while response != 'y' and response != "n" :
        print("mohon di ketik dengan benar")
        response = input("> ")
        response.lower()

        if response == 'y':
            print("selamat kamu punya mobil baru")
        elif response == 'n':
            print("okay terima kasih")
            print("")
            return  get_car(user_option)

def main():
    display_greeting()

if __name__ == '__main__':
    main()
    user_option = get_user_option()
    car_type = get_car(user_option)
    price = get_car_price(car_type)
    get_confirmation(price, car_type, user_option)
