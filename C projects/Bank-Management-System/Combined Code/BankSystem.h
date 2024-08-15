#ifndef BANKSYSTEM_H_INCLUDED
#define BANKSYSTEM_H_INCLUDED

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>

#define sizeUsers 50
#define sizeU 50


///Struct that holds date
typedef struct
{
    int month,year;
} Date;

///Struct that holds all the data for users
typedef struct
{
    char mobile_number[12];
    char account_number[11];
    char username[20];
    char email_address[30];
    double balance;
    Date dateOpened;
    FILE *f_report ;

} Account;

typedef struct
{
    char username[50];
    char password[50];   // i dont know if it should be 50 or more
} User;

///used throughout the program to calculate available places in the accounts array
unsigned int acCount = 0;
unsigned int useCount = 0;
///Array of struct that carries the data of all the users
Account accounts[sizeUsers];
User users[sizeU];

///Main Functions
void readUser(void);
void Login(void);
void loadAccounts(void);
void retrieveData(void);
void Menu(void);
void Add(void);
void deleteAccount(void);
void Modify(void);
void Query(void);
void advSearch(void);
void WithDraw(void);
void Deposit(void);
void Transfer(void);
void Report(void);
void Sort(void);
void Save(void);
void Manual(void);

///Helping functions for struct and arrays manipulation
int   checkAccountNo(char *accStr);
int   checkEmail(char *email);
int   checkName(char *name);
int   checkNumber(char *number);
int   checkBalance(char *BalStr);
int   loadAccIndex(char *accountNumber);
char *convertMonth(int monthnum);
char *StrToUpper(char *str);
int  *sortByDate(void);
int  *sortByBalance(void);
int  *sortByName(void);
void fillArray(int *ptr);


void constructAccount(Account *acc, char *mobile, char *accNum, char *name, char *email, double balanceNum, Date *dateOpnd);
void destructAccount(Account *acc);
void printUser(const Account *user);
int  AccountExistenceCheck (char *accountNumber);


void readUser(void)
{
    int i = 0;

    FILE *file = fopen("users.txt", "r");
    if (file == NULL)
    {
        printf("Error opening users.txt\n");
        exit(-1);
    }

    while (fscanf(file, "%s %s", users[i].username, users[i].password) == 2)
    {
        (useCount)++;
        i++;
    }

    fclose(file);
}

void Login(void)
{
    char username[50];
    char password[50];
    int flag = 0;

    readUser();

    do
    {
        printf("Enter username: ");
        gets(username);
        printf("Enter password: ");
        gets(password);

        for (int i = 0; i < useCount; i++)
        {
            if (strcmp(username, users[i].username) == 0 && strcmp(password, users[i].password) == 0)
            {
                printf("Logged in Successfully!\n");
                flag = 1;
                break;
            }
        }

        if (!flag)
            printf("Incorrect Username or Password!\n");

    }
    while (!flag);
}


void loadAccounts(void)
{
    FILE *file = fopen("accounts.txt", "r");
    if (file == NULL)
    {
        printf("Error opening file: accounts.txt\n");
        return;
    }

    char line[256]; // Adjust the buffer size as needed

    // Read data from the file and populate the accounts array
    while (fgets(line, sizeof(line), file) != NULL)
    {
        // Remove trailing newline character
        //line[strcspn(line, "\n")] = '\0';

        // Use strtok to tokenize the line based on commas
        char *token = strtok(line, ",");
        if (token != NULL)
        {
            strcpy(accounts[acCount].account_number, token);
            token = strtok(NULL, ",");
        }

        if (token != NULL)
        {
            strcpy(accounts[acCount].username, token);
            token = strtok(NULL, ",");
        }

        if (token != NULL)
        {
            strcpy(accounts[acCount].email_address, token);
            token = strtok(NULL, ",");
        }

        if (token != NULL)
        {
            accounts[acCount].balance = atof(token);
            token = strtok(NULL, ",");
        }

        if (token != NULL)
        {
            strcpy(accounts[acCount].mobile_number, token);
            token = strtok(NULL, ",");
        }

        if (token != NULL)
        {
            sscanf(token, "%d-%d",
                   &accounts[acCount].dateOpened.month,
                   &accounts[acCount].dateOpened.year);
        }

        acCount++;
    }

    fclose(file);
}


///Retrieving data from the text file and constructing the instances based on data collected
/*void retrieveData(void)
{
    FILE *fptr = fopen("accounts.txt", "r");
    if (fptr == NULL)
    {
        printf("Couldn't find database file!\n");
        exit(-1);
    }

    char buffer[200];
    size_t i = 0, j;

    while((!feof(fptr)) && i < sizeUsers)
    {
        j = 0;
        fgets(buffer, 200, fptr);

        char *token = strtok(buffer, ",");
        char *dateTok;

        strcpy((accounts + i)->account_number, token);
        while(token != NULL)
        {
            switch(j)
            {
            case 1:
                strcpy((accounts + i)->username, token);
                break;

            case 2:
                strcpy((accounts + i)->email_address, token);
                break;

            case 3:
                (accounts + i)->balance = strtod(token, NULL);
                break;

            case 4:
                strcpy((accounts + i)->mobile_number, token);
                break;

            case 5:
                dateTok = strtok(token, "-");
                //Convert the read token into integer
                (accounts + i)->dateOpened.month = atoi(dateTok);
                while (dateTok != NULL)
                {
                    (accounts + i)->dateOpened.year = atoi(dateTok);
                    dateTok = strtok(NULL, "-");
                }
                break;
            }
            token = strtok(NULL, ",");
            j++;
        }
        i++;
    }
    fclose(fptr);
    ///Set the global accounts counter
    acCount = i - 1;
}
*/

///This function is main caller for all the other functions in the program
///Gives you a list of options to choose from and then interprets the entered data
///to known commands like a CLI
void Menu(void)
{
    char choice[20];
    int flag;
    do
    {
        flag = 0;
        printf("%s", "\n\t******** Main Menu (0o0) ********\n");
        printf("%s", "Please select one of the following options(Enter the EXACT name of desired option as shown below):\n");
        printf("%s", " - ADD\n - DELETE\n - MODIFY\n - SEARCH\n - ADVANCED SEARCH\n - WITHDRAW\n");
        printf("%s", " - DEPOSIT\n - TRANSFER\n - REPORT\n - PRINT\n - MANUAL\n - QUIT\n");
        printf("Desired option: ");
        gets(choice);
        StrToUpper(choice);

        if (strcmp(choice, "ADD") == 0)
            Add();

        else if (strcmp(choice, "DELETE") == 0)
            deleteAccount();

        else if (strcmp(choice, "MODIFY") == 0)
            Modify();

        else if (strcmp(choice, "SEARCH") == 0)
            Query();

        else if (strcmp(choice, "ADVANCED SEARCH") == 0)
            advSearch();

        else if (strcmp(choice, "WITHDRAW") == 0)
            WithDraw();

        else if (strcmp(choice, "DEPOSIT") == 0)
            Deposit();

        else if (strcmp(choice, "TRANSFER") == 0)
            Transfer();

        else if (strcmp(choice, "REPORT") == 0)
            Report();

        else if (strcmp(choice, "PRINT") == 0)
            Sort();

        else if (strcmp(choice, "MANUAL") == 0)
            Manual();

        else if (strcmp(choice, "QUIT") == 0)
        {
            printf("Thank you for using our system :)\nExiting...\n");
            exit(0);
        }
        else
        {
            printf("%s", "Invalid Option Entered!\n");
        }
    }
    while (!flag);
}



void Add(void)
{

/// return a pointer to the current calendar time
    /// variable suitable for storing the calender time since 1970
    time_t t = time(NULL);
    /// instant of time structure and local function breaks the time since 1970 into the structure variables
    struct tm Newtime = *localtime(&t);

    char account_number[11];
    char mobile_number[12];
    char username[20];
    char choice;
    int flag_1 = 0, flag_2 = 0;
    char email_adresss[30];
    double balance = 0;
    Date date2;

    do
    {
        /// print the number of available places
        printf("There are a %d places allowed\n", sizeUsers - acCount);
        printf("%s\n", "----  New Account ---");
        do
        {
            printf("%s", "Account_number : ");

            gets(account_number);

            flag_1 = checkAccountNo(account_number);

            flag_2 = AccountExistenceCheck(account_number);
            if(flag_2 == 0)
            {
                printf("%s\n", "Account already exist!!\n");
            }

        }
        while(flag_1 == 0 || flag_2 == 0);

        do
        {
            printf("%s", "UserName: ");
            gets(username);
            flag_1 = 0;
            flag_1 = checkName(username);
        }
        while(flag_1 == 0);

        do
        {
            flag_1 == 0;
            printf("%s", "Mobile Number: ");
            gets(mobile_number);
            flag_1 = checkNumber(mobile_number);
        }
        while(flag_1 == 0);

        do
        {
            flag_1 = 0;
            printf("%s", "Email Address: ");
            gets(email_adresss);
            flag_1 = checkEmail(email_adresss);
        }
        while(flag_1 == 0);
        /// the data of adding the account
        ///    printf("%d",Newtime.tm_year);
        date2.year = Newtime.tm_year + 1900;
        date2.month = Newtime.tm_mon + 1;
        /// making an instant of the data
        ///     Account *new_client = malloc(sizeof(Account));
        ///   ConstructAccount(new_client, mobile_number, account_number, username, email_adresss, &balance, &data);
        /// increasing the number of accounts
        ++acCount;
        constructAccount(&accounts[acCount - 1], mobile_number, account_number, username, email_adresss, balance, &date2);
        Save();
        ///choice for adding ,more accounts
        printf("Do you want to add more accounts?(Y for Yes/N for No): ");
        scanf("%c", &choice);
        getchar();

    }
    while(choice == 'Y' || choice == 'y');
}


void deleteAccount(void)
{
    char accountNumberToDelete[11];
    int indexToDelete;
    char choice;

    do
    {
        do
        {
            printf("Enter the bank account number to delete: ");
            gets(accountNumberToDelete);

        } while (!(AccountExistenceCheck(accountNumberToDelete) == 0 && checkAccountNo(accountNumberToDelete)== 1));

        // Check if the account exists
        indexToDelete = loadAccIndex(accountNumberToDelete);


        // Check if the balance is zero for deletion
        if (accounts[indexToDelete].balance > 0)
        {
            printf("Error: Deletion of non-zero balance account is not allowed.\n");
        }
        else
        {
        // replace last index and deleted
        // Shift remaining accounts to fill the gap
        for (int i = indexToDelete; i < acCount - 1; i++)
        {
            accounts[i] = accounts[i + 1];
        }

        acCount--;

        // make everything for the account 0

        printf("Account with account number %s has been deleted.\n", accountNumberToDelete);
        // ask if user wants to save
        Save();
        }


        printf("\nDo you want to delete for more accounts?(Y for Yes/N for No): ");
        scanf("%c", &choice);
        getchar();

    }
    while (choice == 'y' || choice == 'Y');
}



void Modify(void)
{
    char accReqMod[11];
    char choice1, choice2;
    int flag=1;

    do
    {
        printf("%s\n", "----  Modify Account ---\n");
        /// check for account length limit
        do
        {
            printf("%s", "Enter account number needed to modify: ");
            gets(accReqMod);

        }
        while(checkAccountNo(accReqMod) == 0);

        /// in case of account do not exist
        if(AccountExistenceCheck(accReqMod) != 0)
        {
            printf("This account don't exist !!\n");
            printf("%s", "[Y] to Add a new account  or [N] to go the Menu : ");
            scanf("%c", &choice2);
            getchar();
            if(choice2 == 'Y' || choice2 == 'y')
            {
                Add();
                flag=0;
            }
            else
                {flag=2;}
        }

        /// modify the required account
        else
        {
            int place = loadAccIndex(accReqMod);
            printf("Do you want to modify on (N for Number,U for Username,E for E-mail: ");
            scanf("%c", &choice2);
            getchar();
            if(choice2 == 'U' || choice2 == 'u')
            {
                do
                {

                    printf("Name: ");
                    gets(accounts[place].username);
                }
                while(checkName(accounts[place].username) == 0);
            }
            else if (choice2 == 'n' || choice2 == 'N')
            {
                do
                {

                    printf("Mobile Number: ");
                    gets(accounts[place].mobile_number);
                    ///check if the user entered the same old number
                }
                while(checkNumber(accounts[place].mobile_number) == 0);
            }
            else if(choice2 == 'e' || choice2 == 'E')
            {
                do
                {

                    printf("E_mail: ");
                    gets(accounts[place].email_address);
                }
                while(checkEmail(accounts[place].email_address) == 0);
            }

            /// if the user entered neither of the choices
            else
            {
                printf("invalid choice\n");
                flag=0;
            }

        }
        if(flag == 1)
          {Save();
          }
        if (flag != 2)
        {printf("\nDo want to modify again?!!\n(Y for yes, N for no)");
        scanf("%c", &choice1);
        getchar();
        }
    }
    while(choice1 == 'y' || choice1 == 'y' );
}


///Search the user names using strstr function
///Sets the upper case as a reference to avoid case sensitivity
void advSearch(void)
{
    char search_key[20];
    char buffer[20];
    char choice = 'y';

    do
    {
        printf("%s", "Enter the search keyword: ");
        gets(search_key);

        int found = 0;

        printf("%s", "Search results:\n\n");
        for (size_t i = 0; i < acCount; i++)
        {
            strcpy(buffer, (accounts + i)->username);
            if (strstr(StrToUpper(buffer), StrToUpper(search_key)) != NULL)
            {
                printUser((accounts + i));
                found = 1;
            }
        }

        if (found == 0)
        {
            printf("No matches are found!\n");
        }
        printf("Do you want to search for something else?(Y/N): ");
        scanf("%c", &choice);
        getchar();
    }
    while (choice == 'y' || choice == 'Y');
}

void Query(void)
{
    char reqAcc[11];
    int flag=0;
    char choise;
    printf("%s\n","----  Search for an Account ---");
    do
    {
        printf("%s\n","Please enter the account number :");
        do
        {
            gets(reqAcc);
            flag=checkAccountNo(reqAcc);
        }
        while(flag==0);
        /// deal with the situation of non existing accounts
        if(AccountExistenceCheck(reqAcc)!=0)
        {
            printf("This account don't exist !!\n");
            printf("%s","[Y] to Add a new account  or [N] to go the Menu : ");
            scanf("%c",&choise);
            getchar();
            if(choise=='Y'||choise=='y')
            {
                Add();
                choise='n';
            }
            else
            {
                break;
            }
        }
        /// load the details of the required account
        else
        {
            /// search for the index of the required account in the main structure of the clients
            int place=loadAccIndex(reqAcc);
            printUser(&accounts[place]);
            printf("\nDo you want to search for more accounts?(Y for Yes/N for No): ");
            scanf("%c", &choise);
            getchar();
        }

    }
    while((choise== 'y' || choise== 'Y'));
}


void WithDraw(void)
{
    char account_number[11];
    char amount1[sizeof(double)];
    double amount2;
    char choice;
    char fileName[16];
    do
    {
        do
        {
            printf("%s", "Enter your account number:");
            gets(account_number);
        }
        while (checkAccountNo(account_number) == 0); //acc num invalid

        if(AccountExistenceCheck(account_number) == 0)//acc exist
        {
            int index = loadAccIndex(account_number);
            printf("Your balance= %.2lf$\n", accounts[index].balance);

            do
            {
                do
                {
                    printf("%s","Enter an amount to withdraw(Max limit=10,000$/transaction): ");
                    gets(amount1);

                }
                while(checkBalance(amount1)==0);
                amount2=strtod(amount1,NULL);
            }
            while(amount2 > 10000 || amount2 > accounts[index].balance || amount2 <= 0);

            accounts[index].balance -= amount2;

            sprintf(fileName, "%s.txt", accounts[index].account_number);
            accounts[index].f_report = fopen(fileName,"a");

            if (accounts[index].f_report == NULL)
            {
                printf("Couldn't Find File!\n");
                exit(-1);
            }
            fprintf(accounts[index].f_report,"Withdraw %0.2lf$\n",amount2);
            fclose(accounts[index].f_report);

            Save();
            printf("Transaction Successful :)\n");

        }

        else
            printf("Transaction Failed!\n");

        printf("Do you want to Withdraw again?(Y/N): ");
        scanf("%c", &choice);
        getchar();
    }
    while (choice == 'y' || choice == 'Y');
}



void Deposit(void)
{
    char account_number[11];
    char amount1[sizeof(double)];
    double amount2;
    char choice;
    char fileName[16];
    do
    {
        do
        {
            printf("%s", "Enter your account number:");
            gets(account_number);


        }
        while (checkAccountNo(account_number) == 0); //acc num invalid

        if(AccountExistenceCheck(account_number) == 0)//acc exist
        {
            do
            {

                do
                {
                    printf("%s", "Enter the amount needs to be deposited (Max limit = 10000$): ");
                    gets(amount1);
                }
                while(checkBalance(amount1)==0);
                amount2=strtod(amount1,NULL);

            }
            while(amount2 > 10000 || amount2 <= 0);


            int index = loadAccIndex(account_number);
            accounts[index].balance += amount2;
            sprintf(fileName, "%s.txt", accounts[index].account_number);
            accounts[index].f_report = fopen(fileName, "a");

            if (accounts[index].f_report == NULL)
            {
                printf("Couldn't find file!\n");
                exit(-1);
            }

            fprintf(accounts[index].f_report, "Deposit %0.2lf$\n", amount2);
            fclose(accounts[index].f_report);
            printf("Transaction successful :)\n");
            Save();
        }

        else
            printf("Transaction failed!\nAccount Not Found!\n");

        printf("\nDo you want to deposit again?(Y/N): ");
        scanf("%c", &choice);
        getchar();
    }
    while (choice == 'y' || choice == 'Y');
}



void Transfer(void)
{
    char account_number1[11];
    char account_number2[11];
    char amount1[sizeof(double)];
    double amount2;
    char choicee;
    char fileName1[16];
    char fileName2[16];
    int flag=0;

    do
    {
        do
        {
            printf("%s", "Enter Sender account number:");
            gets(account_number1);
        }
        while (checkAccountNo(account_number1)==0); //acc num invalid

        do
        {
            printf("%s","Enter Receiver account number:");
            gets(account_number2);
        }
        while (checkAccountNo(account_number2) == 0);  //acc num invalid

        if(AccountExistenceCheck(account_number1) == 0 && AccountExistenceCheck(account_number2) == 0)//acc 1,2 are exist
        {
            int index1 = loadAccIndex(account_number1);
            int index2 = loadAccIndex(account_number2);

            do
            {
                do
                {
                    printf("%s", "Enter an amount to transfer: ");
                    gets(amount1);


                }
                while(checkBalance(amount1)==0);
                amount2=strtod(amount1,NULL);


                if(amount2 > accounts[index1].balance)
                {
                    printf("You only have %lf$ in your account\n", accounts[index1].balance);
                    flag = 1;
                    break;
                }
            }
            while(amount2 < 0);

            if(flag == 0)
            {
                accounts[index1].balance -= amount2;
                accounts[index2].balance += amount2;
                sprintf(fileName1, "%s.txt", accounts[index1].account_number);
                sprintf(fileName2, "%s.txt", accounts[index2].account_number);
                accounts[index1].f_report = fopen(fileName1, "a");
                if(accounts[index1].f_report == NULL)
                {
                    printf("Couldn't Find File!\n");
                    exit(-1);
                }

                fprintf(accounts[index1].f_report, "You sent %0.2lf$ to %s\n", amount2, account_number2);
                fclose(accounts[index1].f_report);

                accounts[index2].f_report = fopen(fileName2, "a");
                if(accounts[index2].f_report == NULL)
                {
                    printf("Couldn't Find File!\n");
                    exit(-1);
                }
                fprintf(accounts[index2].f_report, "You received %0.2lf$ from %s\n", amount2, account_number2);
                fclose(accounts[index2].f_report);

                Save();
                printf("Transaction Successful :)\n");

            }
            else
                printf("Transaction Failed!\n");
        }
        printf("\nDo you want to Transfer again?(Y/N): ");
        scanf("%c", &choicee);
        getchar();
    }
    while (choicee == 'y' || choicee == 'Y');
}



void Report(void)
{
    char account_number[11];
    char fileName[16];
    char buf[100];
    char n;
    int count=0;
    int i;

    do
    {
        printf("%s", "enter your account number:");
        gets(account_number);
    }
    while (checkAccountNo(account_number) == 0); //acc num invalid

    if(AccountExistenceCheck(account_number) == 0)
    {
        sprintf(fileName, "%s.txt", account_number);
        int index=loadAccIndex(account_number);
        accounts[index].f_report=fopen(fileName, "r");
        for(i=0; !feof(accounts[index].f_report); i++)
        {
            n = fgetc(accounts[index].f_report);
            if(n == '\n')
                count++;

        }

        fseek(accounts[index].f_report, 0, SEEK_SET);

        if(count < 5 || count == 5)
        {
            for(i=0; i<count; i++)
            {
                fgets(buf, 99, accounts[index].f_report);
                printf("%s", buf);
            }
        }
        else
        {
            for(i=0; i < (count - 5); i++)
            {
                fgets(buf, 99, accounts[index].f_report);

            }
            for(i=0; i < 5; i++)
            {
                fgets(buf, 99, accounts[index].f_report);
                printf("%s", buf);
            }
        }
        fclose(accounts[index].f_report);
    }
    Menu();

}


void Sort(void)
{
    char c;
    int counter=0,flag=0;
    /// pointer of the index of each account
    int *Indices = NULL;
    do
    {

        printf("%s","please choose the sorting type[ (N) to be sorted by name, (B) to be sorted by balance , (D) to be sorted by date : ");
        scanf("%c", &c);
        getchar();
        if(c == 'N' || c == 'n')
        {
            Indices = sortByName();
            printf("%s","Enter [A] to print from (A to Z) or  [Z] to print from (Z to A)   :");
            do
            {
                scanf("%c",&c);
                getchar();
                /// print the data sorted by names from A to Z
                if(c == 'A'||c == 'a')
                {
                    for( counter = 0; counter<acCount ; ++counter)
                        printUser(&accounts[Indices[counter]]);
                }
                /// print the data sorted by names from Z to A
                else if (c == 'Z' || c == 'z')
                {
                    for( counter = acCount-1; counter>=0 ; --counter)
                        printUser(&accounts[Indices[counter]]);
                }
                else
                {
                    printf("%s","Invalid input!!!\nEnter [A] to print from (A to Z) or  [Z] to print from (Z to A)   :");
                    c=NULL;
                }
            }
            while(c==NULL);
        }

        else if (c == 'B' || c == 'b')
        {
            Indices = sortByBalance();
            printf("in Descending[D] or Ascending[A] order ? ::  ");
            do
            {
                scanf("%c",&c);
                getchar();
                /// print the balances of the accounts in Ascending order
                if(c == 'A' || c == 'a')
                    for( counter = acCount-1; counter>=0 ; --counter)
                        printUser(&accounts[Indices[counter]]);
                /// print the balances of the accounts in Descending order
                else if (c == 'd' || c == 'D')
                    for( counter = 0; counter<acCount ; ++counter)
                        printUser(&accounts[Indices[counter]]);
                else
                {
                    printf("%s","Invalid input!!!\nEnter [D] for Descending or [A] Ascending order:  ");
                    c=NULL;
                }
            }
            while(c == NULL);
        }
        else if (c == 'D' || c == 'd')
        {
            Indices = sortByDate();
            printf("%s","Enter [N] to be sorted from the newest client , [P] to be sorted from the our past client : ");
            do
            {
                scanf("%c",&c);
                getchar();
                if(c == 'N' || c == 'n')

                    for( counter = acCount-1; counter>=0 ; --counter)
                        printUser(&accounts[Indices[counter]]);


                else if (c == 'P' || c == 'p')
                    for( counter = 0; counter<acCount ; ++counter)
                        printUser(&accounts[Indices[counter]]);


                else
                {
                    printf("%s","Invalid input!!!\nEnter [N] to be sorted from the newest client , [P] to be sorted from the our past client : ");
                    c=NULL;
                }
            }
            while(c==NULL);
        }
        else
        {
            printf("%s","Invalid input!!");
            flag=1;
        }

        printf("%s","Do you want to print data in other sorted manners ??( Y for yes , N for No) :: ");
        scanf("%c",&c);
        getchar();
    }
    while(flag==1||c=='Y'||c=='y');
}


int* sortByName(void)
{
    int *Indices = malloc(sizeof(int)*acCount);
    fillArray(Indices);
    int counter_1 = 0,counter_2 = 0,temp;
    /// bubble sorting in A to Z
    for(counter_1 = 0; counter_1<acCount-1; ++counter_1)
    {
        for(counter_2=0; counter_2<acCount-counter_1-1; ++counter_2)
        {
            if(strcmp(accounts[*(Indices+counter_2)].username,accounts[*(Indices+counter_2+1)].username)>0)
            {

                temp = *(Indices+counter_2);
                *(Indices+counter_2) = *(Indices+counter_2+1);
                *(Indices+counter_2+1) = temp;
            }
        }
    }
    return Indices;
}


int* sortByBalance(void)
{
    int *Indices = malloc(sizeof(int)*acCount);
    fillArray(Indices);
    int counter_1 = 0,counter_2 = 0,temp;
/// bubble sorting in A to Z
    for(counter_1 = 0; counter_1<acCount-1; ++counter_1)
    {
        for(counter_2 = 0; counter_2<acCount-counter_1-1; ++counter_2)
        {
            if(accounts[*(Indices+counter_2)].balance<accounts[*(Indices+counter_2+1)].balance)
            {

                temp = *(Indices+counter_2);
                *(Indices+counter_2) = *(Indices+counter_2+1);
                *(Indices+counter_2+1) = temp;
            }
        }
    }
    return Indices;
}


/// fill a default array by number from one
void fillArray(int *ptr)
{
    for(int counter=0; counter<acCount; ++counter)
    {
        *(ptr+counter)=counter;
    }
}


int * sortByDate(void)
{
    int *Indices = malloc(sizeof(int)*acCount);
    fillArray(Indices);
    int counter_1 = 0,counter_2 = 0,temp;
    /// bubble sorting to the years from the oldest
    for(counter_1 = 0; counter_1<acCount-1; ++counter_1)
    {
        for(counter_2 = 0; counter_2<acCount-counter_1-1; ++counter_2)
        {
            int date_1,date_2;
            date_1 = accounts[*(Indices+counter_2)].dateOpened.month;
            date_2 = accounts[*(Indices+counter_2+1)].dateOpened.month;
            // printf("date_1 : %d\ndate_2 : %d\n",date_1,date_2);
            if(date_2<date_1)
            {
                temp = *(Indices+counter_2);
                *(Indices+counter_2) = *(Indices+counter_2+1);
                *(Indices+counter_2+1) = temp;
            }
        }
    }
    /// bubble sorting for the months
    for(counter_1 = 0; counter_1<acCount-1; ++counter_1)
    {
        for(counter_2 = 0; counter_2<acCount-counter_1-1; ++counter_2)
        {
            int date_1,date_2;
            date_1 = accounts[*(Indices+counter_2)].dateOpened.year;
            date_2 = accounts[*(Indices+counter_2+1)].dateOpened.year;
            // printf("date_1 : %d\ndate_2 : %d\n",date_1,date_2);
            if(date_2<date_1)
            {
                temp = *(Indices+counter_2);
                *(Indices+counter_2) = *(Indices+counter_2+1);
                *(Indices+counter_2+1) = temp;
            }
        }
    }

    return Indices;
}


///This function sends all the data collected in the program to the database again
///Data is saved in the format account number, user name, email, balance, mobile number, date opened
void Save(void)
{
    char choice;
    printf("Do you want to save changes?(Y for Yes/N for No): ");
    scanf("%c", &choice);
    getchar();
    if (choice == 'y' || choice == 'Y')
    {
        FILE *fptr = fopen("accounts.txt", "w");

        for (size_t i = 0; i < acCount; i++)
        {
            fprintf(fptr, "%s,", accounts[i].account_number);
            fprintf(fptr, "%s,", accounts[i].username);
            fprintf(fptr, "%s,", accounts[i].email_address);
            fprintf(fptr, "%.2lf,", accounts[i].balance);
            fprintf(fptr, "%s,", accounts[i].mobile_number);
            fprintf(fptr, "%d-%d\n", accounts[i].dateOpened.month, accounts[i].dateOpened.year);
        }

        fclose(fptr);
    }
}


///Printing the user manual that contains details about using the program
void Manual(void){
    printf("\n===========================\nWelcome to the User Manual\n===========================\n\n");
    printf("You'll find a detailed explanation of each function in this program along with the guidelines for data to be entered\n");

    printf("\n1) ADD:\n-------\n - This function is used to add new account to the database with 0.0 balance\n");
    printf(" - It asks you to enter the account number which MUST be 10-digits long and doesn't contain any characters\n");
    printf(" - After entering an existing account number you will be asked to enter the mobile phone which must be 11-digits long \n and doesn't contain any characters\n");
    printf(" - Then you enter the E-mail address which is one of our supported platforms (Gmail, Outlook, Alexu.edu.eg, Yahoo) and\n it must not contain ','\n");
    printf(" - To save your data to the database you should type Y or y when the program asks you if you want to save\n");
    printf(" - You are allowed to add other accounts without going back to the menu by typing Y or y when the program asks you\n");
    printf(" - If you want to add balance use the function Deposit\n");

    printf("\n 2) Delete:\n-----------\n - This function is used to delete accounts in the database\n");
    printf(" - It asks you to enter the account number which MUST be 10-digits long and doesn't contain any characters\n");
    printf(" - This function deletes ONLY accounts that have 0.0 balance\n");
    printf(" - To save your data to the database you should type Y or y when the program asks you if you want to save\n");
    printf(" - You are allowed to delete other accounts without going back to the menu by typing Y or y when the program asks you\n");

    printf("\n 3) Modify:\n-----------\n - This function is used to modify accounts in the database\n");
    printf(" - It asks you to enter the account number which MUST be 10-digits long and doesn't contain any characters\n");
    printf(" - After entering an existing account number you are to choose between three options Name, Email, Mobile number\n");
    printf(" - To save your data to the database you should type Y or y when the program asks you if you want to save\n");
    printf(" - You are allowed to modify other accounts without going back to the menu by typing Y or y when the program asks you\n");

    printf("\n 4) Search:\n-----------\n - This function is used to search for an entered account number in the database\n");
    printf(" - It asks you to enter the account number which MUST be 10-digits long and doesn't contain any characters\n");
    printf(" - You are allowed to search for other accounts without going back to the menu \n by typing Y or y when the program asks you\n");

    printf("\n 5) Advanced Search:\n--------------------\n - This function is used to search for a keyword related to user names in the database\n");
    printf(" - It asks you to enter the Keyword to search for\n");
    printf(" - All the accounts that have the keyword in the user name will be printed on the screen\n");
    printf(" - You are allowed to search for other Keywords without going back to the menu \n by typing Y or y when the program asks you\n");

    printf("\n 6) Withdraw:\n-------------\n - This function is used to withdraw money from an account in the database\n");
    printf(" - It asks you to enter the account number which MUST be 10-digits long and doesn't contain any characters\n");
    printf(" - After entering an existing account number you will be asked to enter the amount of money to be withdrawn\n");
    printf(" - The amount of money shouldn't exceed 10000$ per transaction and must be digits ONLY\n");
    printf(" - To save your data to the database you should type Y or y when the program asks you if you want to save\n");
    printf(" - You are allowed to withdraw again without going back to the menu by typing Y or y when the program asks you\n");

    printf("\n 7) Deposit:\n------------\n - This function is used to deposit money from to an account in the database\n");
    printf(" - It asks you to enter the account number which MUST be 10-digits long and doesn't contain any characters\n");
    printf(" - After entering an existing account number you will be asked to enter the amount of money to be depositted\n");
    printf(" - The amount of money shouldn't exceed 10000$ per transaction and must be digits ONLY\n");
    printf(" - To save your data to the database you should type Y or y when the program asks you if you want to save\n");
    printf(" - You are allowed to deposit again without going back to the menu by typing Y or y when the program asks you\n");

    printf("\n 8) Transfer:\n-------------\n - This function is used to transfer money from to an account to another account in the database\n");
    printf(" - It asks you to enter the sender account number which MUST be 10-digits long and doesn't contain any characters\n");
    printf(" - It asks you to enter the receiver account number which MUST be 10-digits long and doesn't contain any characters\n");
    printf(" - After entering an existing account numbers you will be asked to enter the amount of money to be transfered\n");
    printf(" - The amount of money shouldn't exceed 10000$ per transaction and must be digits ONLY\n");
    printf(" - To save your data to the database you should type Y or y when the program asks you if you want to save\n");
    printf(" - You are allowed to transfer again without going back to the menu by typing Y or y when the program asks you\n");

    printf("\n 9) Report:\n-----------\n - This function is used to print the history of last five transactions for an account in the database\n");
    printf(" - It asks you to enter the account number which MUST be 10-digits long and doesn't contain any characters\n");
    printf(" - The history for the transactions will be presented on the screen\n");
    printf(" - You are allowed to print the report for other account without going back to the menu \n by typing Y or y when the program asks you\n");

    printf("\n 10) Print:\n-----------\n - This function is used to print the accounts in the database in a sorted manner\n");
    printf(" - It asks you to choose the way of sorting (By date, By names, By balance)\n");
    printf(" - The program will ask you to choose the arrangement order -> A for Ascending -> Z for descending\n");
    printf(" - You are allowed to print accounts without going back to the menu \n by typing Y or y when the program asks you\n");


    printf("\n 11) Manual:\n------------\n - If you have reached this point already, we bet that you figured it out yourself :)\n");

    printf("\n 12) Quit:\n----------\n  - Used to quit the program\n\n");

    printf("13) Menu handling:\n------------------\n  - You are free to use upper or lower case letters when choosing the desired option\n");
    printf(" - You have to write the operation name EXACTLY as shown on the menu screen\n");
    printf(" - You will find yourself at the menu right after logging in and after performing any operation from the operations listed above\n");
}

/// return the index of the required client
int loadAccIndex(char *accountNumber)
{

    int counter=0;
    for(counter; counter<acCount; ++counter)
    {
        if(strcmp(accountNumber,accounts[counter].account_number)==0)
            return counter;
    }
}


///return 0 if the account already exist
///return 1 if the account do not exist
/// check existence of an account number
int AccountExistenceCheck (char *accountNumber)
{
/// Add new account
    int counter,flag=0;
    for(counter=0; counter<acCount; ++counter)
    {
        flag=strcmp(accountNumber,accounts[counter].account_number);

        if(flag==0)
        {
            return flag;
        }
    }
    ///printf("%s","account is not exist\n");
    return flag;
}


///Checking the account number errors
///Returns 1 if the input is valid
///Returns 0 if the input isn't valid
int checkAccountNo(char *accStr)
{
    if (strlen(accStr) != 10)
    {
        printf("Invalid Account Number!(Should be 10-Digits)\n");
        return 0;
    }
    for (size_t i = 0; *(accStr + i) != '\0'; i++)
    {
        if (!(isdigit(*(accStr + i)) == 1))
        {
            printf("Invalid Account Number!(Should be numbers ONLY)\n");
            return 0;
        }
    }
    return 1;
}


///Checking the balance errors
///Returns 1 if the input is valid
///Returns 0 if the input isn't valid
int checkBalance(char *BalStr)
{
    for (size_t i = 0; *(BalStr + i) != '\0'; i++)
    {
        if (!((isdigit(*(BalStr + i)) == 1) ||  (*(BalStr + i)=='.' )))
        {
            printf("Invalid Balance!(Should be numbers ONLY)\n");
            return 0;
        }

    }
    return 1;
}


///Checking the name
///Returns 1 if the number is valid
///returns 0 if the number isn't valid
int checkName(char *name)
{
    for (size_t i = 0; *(name + i) != '\0'; i++)
    {
        if (isdigit(*(name + i)) ||  *(name + i) == ',')
        {
            printf("Invalid Name!(Should letters ONLY and not contains ',')\n");
            return 0;
        }
    }
    return 1;
}


///Checking the Email
///Returns 1 if the number is valid
///returns 0 if the number isn't valid
int checkEmail(char *email)
{
    int counter = 0;
    for(size_t i = 0; *(email + i) != '\0'; i++){
        if (*(email + i) == '@')
            counter++;
    }
    if (counter > 1)
    {
        printf("Invalid Email!(Shouldn't contain more than one @)\n");
        return 0;
    }
    else {
        if (!(strstr(email, "@gmail.com") == NULL))
        {

            return 1;
        }
        if (!(strstr(email, "@alexu.edu.eg") == NULL))
        {

            return 1;
        }
        if (!(strstr(email, "@outlook.com") == NULL))
        {

            return 1;
        }

        if (!(strstr(email, "@yahoo.com") == NULL))
        {

            return 1;
        }

        else
        {
            printf("Invalid E-mail!!!\n");
            return 0;
        }
    }
}


///Checking the mobile number
///Returns 1 if the number is valid
///returns 0 if the number isn't valid
int checkNumber(char *number)
{
    if (strlen(number) != 11)
    {
        printf("Invalid Mobile Number!(Should contain 11 numbers)\n");
        return 0;
    }

    for (size_t i = 0; *(number + i) != '\0'; i++)
    {
        if (isalpha(*(number + i)) || *(number + i) == ',')
        {
            printf("Invalid Mobile Number!(Shouldn't contain letters and not ',')\n");
            return 0;
        }
    }

    return 1;
}


///Testing that the data is saved properly
void printUser(const Account *user)
{
    printf("Account number: %s\n", user->account_number);
    printf("Name: %s\n", user->username);
    printf("E-mail : %s\n", user->email_address);
    printf("Balance: %.2lf$\n", user->balance);
    printf("Mobile: %s\n", user->mobile_number);
    printf("Date Opened: %s %d\n", convertMonth(user->dateOpened.month), user->dateOpened.year);
    printf("\n");
}


///Will be mainly used in ADD function
void constructAccount(Account *acc, char *mobile, char *accNum, char *name, char *email, double balanceNum, Date *dateOpnd)
{
    ///Copying the arguments into the new instance arguments
    strcpy(acc->account_number, accNum);
    strcpy(acc->mobile_number, mobile);
    strcpy(acc->email_address, email);
    strcpy(acc->username, name);
    acc->balance = balanceNum;
    acc->dateOpened.month = dateOpnd->month;
    acc->dateOpened.year = dateOpnd->year;
}


///Will be used before closing the program
void destructAccount(Account *acc)
{
    free(acc);
}


///Function that changes all the characters in a string to UPPER case
char *StrToUpper(char *str)
{
    for (size_t i = 0; str[i] != '\0'; i++)
        *(str + i) = toupper(*(str + i));
    return str;
}


char *convertMonth(int monthnum)
{
    switch(monthnum)
    {
    case 1:
        return "January";
    case 2:
        return "February";
    case 3:
        return "March";
    case 4:
        return "April";
    case 5:
        return "May";
    case 6:
        return "June";
    case 7:
        return "July";
    case 8:
        return "August";
    case 9:
        return "September";
    case 10:
        return "October";
    case 11:
        return "November";
    case 12:
        return "December";
    }
}
/*int checkinput(char *input)
{
if(strcmp(input,"Y")==0)
{
return 1;
}
else if(strcmp(input,"y")==0)
{
return 1;
}
else if(strcmp(input,"yes")==0)
{
return 1;
}
else if(strcmp(input,"Yes")==0)
{
return 1;
}
else if(strcmp(input,"Yes")==0)
{
return 1;
}
else
{
return 0;
}

}
*/
#endif // BANKSYSTEM_H_INCLUDED
