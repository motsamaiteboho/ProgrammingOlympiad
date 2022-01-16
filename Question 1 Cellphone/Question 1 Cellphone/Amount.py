class Amount(object):
    """description of class"""
def PrintAmount(DayTime, Evening, Weekends):
  amount =0;
  if DayTime > 100:
    amount += (DayTime - 100) * 80
 
  amount += Evening * 70
  amount += Weekends * 50
  return amount

