#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include "student.h"

void initial(struct Students **list) {
    if (list == NULL) return;
    *list = (struct Students *)malloc(sizeof(struct Students));
    (*list)->capacity = 2;
    (*list)->members = (Student **)malloc(2 * sizeof(Student));
    (*list)->members[0] = NULL;
    (*list)->members[1] = NULL;
    (*list)->length = 0;
}

int availableSpots(struct Students *list) {
    assert(list != NULL);
    
    return STUDENTS_MAX - list->length;
}

Student *add(struct Students *list, int id, char *name) {
    assert(list != NULL);
    
    if (list->length == STUDENTS_MAX) {
        printf("No room to accept new student\n");
        return NULL;
    }
    
    Student *m = seek(list, id);
    if (m != NULL) {
        printf("ID %d exists, choose another one.\n", id);
        return NULL;
    }
    
    int l = 0;
    if (name != NULL) {
        l = strlen(name);
        if (l >= NAME_MAX) {
            printf("Length of name exceeded, must less than %d\n", NAME_MAX);
            return NULL;
        }
    }
    

    m = (Student *)malloc(sizeof(Student));
    m->studentID = id;
    if (name != NULL) {
        strcpy(m->name, name);
        m->name[l] = '\0';
    } else
        m->name[0] = '\0';
    
    if (list->length == list->capacity) {
        list->members = (Student **)realloc(list->members, ++list->capacity * sizeof(Student *));
        if (list->members == NULL) {
            printf("Failed to extend student list\n");
            return NULL;
        }
        list->members[list->length++] = m;
    } else {
        for (int i = 0; i < list->capacity; i++) {
            if (list->members[i] == NULL) {
                list->members[i] = m;
                list->length++;
                break;
            }
        }
    }
    
    int c;
    if ((c = availableSpots(list)) == 0){
        printf("You have reached the maximum capacity of the class. ");
        printMembers(list);
    }
            
    return m;
}

Student *seek(struct Students *list, int id) {
    assert(list != NULL);
    
    Student *m;
    for (int i = 0; i < list->capacity; i++) {
        m = list->members[i];
        if (m != NULL && m->studentID == id)
            return m;
    }
    return NULL;
}

void named(Student *student, char *name) {
    assert(student != NULL);
    assert(name != NULL);
    
    int l = strlen(name);
    strcpy(student->name, name);
    student->name[l] = '\0';
}

void drop(struct Students *list, int id) {
    assert(list != NULL);

    Student *member;
    for (int i = 0; i < list->capacity; i++) {
        member = list->members[i];
        if (member != NULL && member->studentID == id) {
            free(member);
            list->length--;
            return;
        }
    }
}

void printMembers(struct Students *list) {
    assert(list != NULL);
    printf("You have %d students in the class:\n", list->length);

    Student *member;
    for (int i = 0; i < list->capacity; i++)
        if (list->members[i] != NULL) {
            member = list->members[i];
            printf("%d, %s\n", member->studentID, member->name);
        }
}

void destroy(struct Students **list) {
    if (list == NULL) return;
    
    Student *m;
    for (int i = 0; i < (*list)->capacity; i++) {
        m = (*list)->members[i];
        if (m != NULL) {
            free(m);
            (*list)->length--;
        }
    }
    free((*list)->members);
    free(*list);
}


int main(void) {
    struct Students *students = NULL;
    initial(&students);
    
    Student *member;
    int op = -1;
    int c;
    int id;
    char name[NAME_MAX];
    char *pos;
    for (;;) {
        printf("Enter operation: ");
        scanf("%d", &op);
        c = availableSpots(students);
        switch (op) {
        case 1:
            printf("Enter ID to add (%d spots available): ", c);
            scanf("%d", &id);
            printf("Enter student name: ");
            scanf("%s", name);
            pos = strchr(name, '\n');
            if (pos != NULL)
                *pos = '\0';
            member = add(students, id, name);
            assert(member != NULL);
            continue;
        case 2:
            printf("Enter ID to drop: ");
            scanf("%d", &id);
            drop(students, id);
            continue;
        case 0:
            printMembers(students);
            break;
        default:
            printf("Illegal operation: %d, valid choosen are 1 (add), 2(drop) and 0(quit program)\n", op);
            continue;
        }
        break;
    }
    
    destroy(&students);
    return 0;
}

