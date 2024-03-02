#include <stdio.h>
#include "autoconfig.h"
int main()
{
    printf("hello, world\n");
#ifdef CONFIG_TEST_ENABLE
    printf("CONFIG_TEST_ENABLE\n");
#endif
	printf("CONFIG_TEST_SHOW_STRING: %s\n", CONFIG_TEST_SHOW_STRING);
	printf("CONFIG_TEST_SHOW_INT: %d\n", CONFIG_TEST_SHOW_INT);
#ifdef CONFIG_TEST_TOP_ENABLE
    printf("CONFIG_TEST_TOP_ENABLE\n");
#endif
#ifdef CONFIG_TEST_SUB_0_ENABLE
    printf("CONFIG_TEST_SUB_0_ENABLE\n");
#endif
#ifdef CONFIG_TEST_SUB_1_ENABLE
    printf("CONFIG_TEST_SUB_1_ENABLE\n");
#endif
	printf("CONFIG_TEST_SHOW_SUB_INT: %d\n", CONFIG_TEST_SHOW_SUB_INT);
    return 0;
}
————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。
                        
原文链接：https://blog.csdn.net/wenbo13579/article/details/127464764