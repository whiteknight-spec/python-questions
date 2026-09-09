# 2) generate the below pattern
#     ```
#         *
#        **
#       ***
#      ****
#     *****
#     ```

a=5
for i in range(1,a+1):
    print(" "*(a-i)+"*"*i)
    