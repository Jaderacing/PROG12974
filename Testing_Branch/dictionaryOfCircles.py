import mycircle1
import pickle
#Program to process a dictionary of circles
def main():

    #display_circles()
    view_specific_circle()
   
def view_specific_circle():
    end_of_file = False
    input_file = open('circlefile.dat','rb')
    cir_dict = {}
    while not end_of_file:
        try:
            cir = pickle.load(input_file)
            cir_dict[cir.get_radius()] = cir

            print(f'Radius is {cir.get_radius():.2f}\n')
            print(f'Color is {cir.get_color()}\n')
            print(f'Area is {cir.calc_area():.2f}\n')
            print(f'Circumference is {cir.calc_circum():.2f}\n')
            cir.draw_circle()
        except EOFError:
            end_of_file = True
    input_file.close()

    for key in cir_dict:
        print(f'[Key is] {key}\n[Value is] {cir_dict[key]} {cir_dict[key].calc_area()}')
    
    radius_key = int(input('Enter Circle Radius to Process'))
    if radius_key in cir_dict:
        print(f'Radius is {cir_dict[radius_key].get_radius():.2f}\n')
        print(f'Color is {cir_dict[radius_key].get_color()}\n')
        print(f'Area is {cir_dict[radius_key].calc_area():.2f}\n')
        print(f'Circumference is {cir_dict[radius_key].calc_circum():.2f}\n')
        cir_dict[radius_key].draw_circle()
    else:
        print(f'Radius {radius_key} not found')





if __name__ == '__main__' :
    main()
