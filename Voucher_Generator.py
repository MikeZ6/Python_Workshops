"""
Author: Mike Zhang

The program shown prints out a lucky draw coupon as shown and allow a batch printing of coupons.
User can select reference to the first draw number and how many to print for the following.

Sample:
  Please enter the reference no for the voucher : 5678
====================================================================================================
NTU                                    Annual Dinner & Dance                    Lucky Draw No : 5678
====================================================================================================

      The Lucky Draw will be conducted after the dinner,
      please keep this coupon in exchange of your gift 
"""

def LuckyDraw():
    startVNo = int(input("Please enter the reference no for the first voucher : "))
    nos = int(input("Please enter the number of vouchers required : "))
    for i in range(nos):
        pgno = startVNo + i
        
        Left_Header = "NTU"
        Center_Header = f"Annual Dinner & Dance"
        DrawNo_Text = f"Lucky Draw No : {pgno}"
    
        print("="*100)
        print(f"{Left_Header:<20}{Center_Header:^60}{DrawNo_Text:>20}")
        print("="*100)
        print('''
              The Lucky Draw will be conducted after the dinner,
              please keep this coupon in exchange of your gift 
              ''')
        print("-"*100)
   
if __name__ == "__main__":
    LuckyDraw()