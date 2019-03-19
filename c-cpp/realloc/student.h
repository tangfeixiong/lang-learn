
#define STUDENTS_MAX 5
#define NAME_MAX 20

typedef struct {
    int studentID;
    char name[20];
} Student;

struct Students{
    Student **members;
    int capacity;
    int length;
};

void initial(struct Students **list);
int availableSpots(struct Students *list);
Student *add(struct Students *list, int id, char *name);
Student *seek(struct Students *list, int id);
void named(Student *student, char *name);
void drop(struct Students *list, int id);
void printMembers(struct Students *list);
void destroy(struct Students **list);