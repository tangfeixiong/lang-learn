
typedef struct {
    int hours;
    int minutes;
    int seconds;
} time;

time secondstohms(int totalseconds);

int secondstotime(int totalseconds, int* days, int* hours, int* minutes, int* seconds);