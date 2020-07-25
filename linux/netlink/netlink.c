/*
Google: inotify /sys/class/net
https://stackoverflow.com/questions/26672414/inotify-add-watch-fails-on-sys-class-net-eth0-operstate
*/

#include <errno.h>
#include <stdio.h>
#include <string.h>
#include <asm/types.h>
#include <asm/types.h>
#include <sys/socket.h>
#include <linux/netlink.h>
#include <linux/if.h>
#include <linux/rtnetlink.h>

#define ENTRY(x) {x, #x}
struct {
    unsigned flag;
    const char *name;
} ifi_flag_map[] = {
    ENTRY(IFF_UP),
    ENTRY(IFF_BROADCAST),
    ENTRY(IFF_DEBUG),
    ENTRY(IFF_LOOPBACK),
    ENTRY(IFF_POINTOPOINT),
    ENTRY(IFF_NOTRAILERS),
    ENTRY(IFF_RUNNING),
    ENTRY(IFF_NOARP),
    ENTRY(IFF_PROMISC),
    ENTRY(IFF_ALLMULTI),
    ENTRY(IFF_MASTER),
    ENTRY(IFF_SLAVE),
    ENTRY(IFF_MULTICAST),
    ENTRY(IFF_PORTSEL),
    ENTRY(IFF_AUTOMEDIA),
    ENTRY(IFF_DYNAMIC),
    ENTRY(IFF_LOWER_UP),
    ENTRY(IFF_DORMANT),
    ENTRY(IFF_ECHO),
};
struct {
    unsigned type;
    const char *name;
} nlmrt_type_map[] = {
    ENTRY(RTM_NEWLINK ),
    ENTRY(RTM_DELLINK),
    ENTRY(RTM_GETLINK),
    ENTRY(RTM_SETLINK),
    ENTRY(RTM_NEWADDR ),
    ENTRY(RTM_DELADDR),
    ENTRY(RTM_GETADDR),
    ENTRY(RTM_NEWROUTE    ),
    ENTRY(RTM_DELROUTE),
    ENTRY(RTM_GETROUTE),
    ENTRY(RTM_NEWNEIGH    ),
    ENTRY(RTM_DELNEIGH),
    ENTRY(RTM_GETNEIGH),
    ENTRY(RTM_NEWRULE ),
    ENTRY(RTM_DELRULE),
    ENTRY(RTM_GETRULE),
    ENTRY(RTM_NEWQDISC    ),
    ENTRY(RTM_DELQDISC),
    ENTRY(RTM_GETQDISC),
    ENTRY(RTM_NEWTCLASS   ),
    ENTRY(RTM_DELTCLASS),
    ENTRY(RTM_GETTCLASS),
    ENTRY(RTM_NEWTFILTER  ),
    ENTRY(RTM_DELTFILTER),
    ENTRY(RTM_NEWACTION   ),
    ENTRY(RTM_DELACTION),
    ENTRY(RTM_GETACTION),
    ENTRY(RTM_NEWPREFIX   ),
    ENTRY(RTM_GETMULTICAST ),
    ENTRY(RTM_GETANYCAST  ),
    ENTRY(RTM_NEWNEIGHTBL ),
    ENTRY(RTM_GETNEIGHTBL ),
    ENTRY(RTM_SETNEIGHTBL),
    ENTRY(RTM_NEWNDUSEROPT ),
    ENTRY(RTM_NEWADDRLABEL ),
    ENTRY(RTM_DELADDRLABEL),
    ENTRY(RTM_GETADDRLABEL),
    ENTRY(RTM_GETDCB ),
    ENTRY(RTM_SETDCB),
    ENTRY(RTM_NEWNETCONF ),
    ENTRY(RTM_GETNETCONF ),
    ENTRY(RTM_NEWMDB ),
    ENTRY(RTM_DELMDB ),
    ENTRY(RTM_GETMDB ),
};

void print_type(unsigned type)
{
    size_t i;

    for (i = 0; i < sizeof nlmrt_type_map/sizeof nlmrt_type_map[0]; i++) {
        if (type == nlmrt_type_map[i].type) {
            printf("\t\tMsg Type: %s\n", nlmrt_type_map[i].name);
            return;
        }
    }

    printf("\t\tMsg Type: unknown(%d)\n", type);
}
void print_flags(unsigned flags, unsigned change)
{
    size_t i;

    printf("\t\tflags: ");

    for (i = 0; i < sizeof ifi_flag_map/sizeof ifi_flag_map[0]; i++) {
        if (flags & ifi_flag_map[i].flag) {
            if (change & ifi_flag_map[i].flag) {
                printf("%s(C) ", ifi_flag_map[i].name);
            } else {
                printf("%s ", ifi_flag_map[i].name);
            }
        }
    }
    puts("");
}
oid read_msg(int fd)
{
    int len;
    char buf[4096];
    struct iovec iov = { buf, sizeof(buf) };
    struct sockaddr_nl sa;
    struct msghdr msg = { (void *)&sa, sizeof(sa), &iov, 1, NULL, 0, 0 };
    struct nlmsghdr *nh;

    len = recvmsg(fd, &msg, 0);
    if(len == -1) {
        perror("recvmsg");
        return;
    }

    for (nh = (struct nlmsghdr *) buf; NLMSG_OK (nh, len);
         nh = NLMSG_NEXT (nh, len)) {
         struct ifinfomsg *ifimsg;
        /* The end of multipart message. */
         printf("netlink message: len = %u, type = %u, flags = 0x%X, seq = %u, pid = %u\n",
            nh->nlmsg_len,
            nh->nlmsg_type,
            nh->nlmsg_flags,
            nh->nlmsg_seq,
            nh->nlmsg_pid);

        if (nh->nlmsg_type == NLMSG_DONE)
            return;

       if (nh->nlmsg_type == NLMSG_ERROR) {
            continue;
       }

       ifimsg = NLMSG_DATA(nh);
       printf("\tifi_family = %u, ifi_type = %u, ifi_index = %u, ifi_flags = 0x%X, ifi_change = 0x%X\n",
               ifimsg->ifi_family ,
               ifimsg->ifi_type ,
               ifimsg->ifi_index ,
               ifimsg->ifi_flags ,
               ifimsg->ifi_change);
       print_type(nh->nlmsg_type);
       print_flags(ifimsg->ifi_flags, ifimsg->ifi_change);
    }
}
int main(int argc, char *argv[])
{
    struct sockaddr_nl sa;
    int fd;

    memset(&sa, 0, sizeof(sa));
    sa.nl_family = AF_NETLINK;
    sa.nl_groups = RTMGRP_LINK | RTMGRP_IPV4_IFADDR;

    fd = socket(AF_NETLINK, SOCK_RAW, NETLINK_ROUTE);
    if(fd == -1) {
        perror("socket");
        return 1;
    }

    if(bind(fd, (struct sockaddr *) &sa, sizeof(sa)) == -1) {
        perror("bind");
        return 1;
    }
    for(;;) {
        read_msg(fd);
    }

    return 0;
}