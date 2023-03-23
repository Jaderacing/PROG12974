import mycircle1
import pickle

#Program to process a file of circles
def main():
    create_circle_file()
    
   

def create_circle_file():
    output_file = open('circlefile.dat','wb')

    numberOfCircles = int(input('How many circles to process? '))
    for count in range(numberOfCircles):
        newradius = float(input(f'Circle #{count+1} radius: '))
        newcolor = input(f'Circle #{count+1} color: ')
        circle_obj = mycircle1.circle(newradius, newcolor)
        pickle.dump(circle_obj,output_file)
    output_file.close()
    print(f'File created with {numberOfCircles} circles')
  
if __name__ == '__main__' :
    main()
