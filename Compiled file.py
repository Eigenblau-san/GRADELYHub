import STUDENT_MGMT
import ADD_SUBJ
import COMPUTE_GRADE_LEC
import COMPUTE_LAB
import LecLabGradeDraft

def main_menu():
    while True:
        print('\n----------Main Menu----------')
        print('1. Student Management')
        print('2. Add Subject')
        print('3. Compute Grade (Lecture Only)')
        print('4. Compute Grade (Laboratory)')
        print('5. Compute Grade (Lecture and Laboratory)')
        print('6. Exit Program')
        
        #User input choice
        choice = input('Enter program (1-6): ').strip()
        
        if choice == '1':
            print('\nProgram 1 running...')
            STUDENT_MGMT.main()
        elif choice == '2':
            print('\nProgram 2 running...')
            ADD_SUBJ.main()
        elif choice == '3':
            print('\nProgram 3 running...')
            COMPUTE_GRADE_LEC.main()
        elif choice == '4':
            print('\nProgram 4 running...')
            COMPUTE_LAB.main()
        elif choice == '5':
            print('\nProgram 5 running...')
            LecLabGradeDraft.main()
        elif choice == '6':
            print('\nExiting Program...')
            break #program ends
        else:
            print('invalid choice!')
            
if __name__ == '__main__':
    main_menu()