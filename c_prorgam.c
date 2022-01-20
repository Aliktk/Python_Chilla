// C++ program to store data of an employee in a structure variable
#include <iostream>
using namespace std;
 
struct employees_data {
    char emp_name[50];
    int emp_id;
    char emp_department;
    int emp_cell;
    char emp_add[50];
    int emp_sal;

};
 
int main() {

    employees_data ed;  
    employees_data ed, temp;
    temp = getData(ed);
    ed = temp;
    // Function call with structure variable as an argument

    displayData(ed);
    search(array);
    int res = findMax(arr, 5);
    cout << "max :: " << res << endl;
    return 0;
}

    
// get data function
employees_data getData(employees_data ed) {

    cout << "Enter name of employee : ";
    cin.getline(ed.emp_name, 50);
    cout << "Enter ID of department : ";
    cin.getline(ed.emp_id, 5);
    cout << "Enter Department of employee : ";
    cin >> ed.emp_department;
    cout << "Enter employee Cell No : ";
    cin >> ed.emp_cell;
    cout << "Enter employee Address : ";
    cin >> ed.emp_add;
    cout << "Enter employee Salery : ";
    cin >> ed.emp_sal;

    return ed;
}
//int n
void displayData(employees_data ed ) {
cout << "\nDisplaying Information." << endl;
cout << "Name of employee :: " << ed.emp_name << endl;
cout <<"ID of employee: " << ed.emp_id << endl;
cout << "Department of employee: " << ed.emp_department;
cout <<"Salary of employee: " << ed.emp_cell << endl;
cout << "Cell No of employee: " << ed.emp_add;
}


void search(employees_data array[])
{
    char first;
    cout << "Enter name";
    cin >> first;

    for(int i = 0; i < 10; i++) {
        if(array[i].f_name == first ) {
            displayData(array[i]);
        }
    }
    return first;
}
int findMax(employees_data arr[], int n)
{
    int mx = 2; //it could be any number here its not that much customized
    for (int i = 0; i < n; i++) {
        int temp = 12 * (arr[i].feet) 
                     + arr[i].inches;
        mx = max(mx, temp);
    }
    return mx;
}

