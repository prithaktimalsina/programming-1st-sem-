class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    @staticmethod
    def _format(unit):
        return str(unit) if unit > 9 else '0' + str(unit)    
        
    @staticmethod
    def _time_to_seconds(time):
        return time.hours * 360 + time.minutes * 60 + time.seconds  
    
    @staticmethod
    def _seconds_to_time(seconds):
        hours = seconds // 3600
        seconds -= hours * 3600
        minutes = seconds // 60
        seconds -= minutes * 60
        return Time(hours, minutes, seconds) 
        
    def __str__(self):
        return str(self.hours) + ":" + Time._format(self.minutes) + ":" + Time._format(self.seconds)
    
    def __add__(self, other):
        if isinstance(other, Time):
            return Time._second_to_time(Time._time_to_seconds(self) + Time._time_to_seconds(other))
        if isinstance(other, int):
            return Time._second_to_time(Time._time_to_seconds(self)+other)
        else:
         

    def __gt__(self, other):
        return True if Time._time_to_seconds(self) > Time._time_to_seconds(other) else False
    
t1 = Time(5,34,23)
t2 = Time(8,37,57)
s1 = Time._time_to_seconds(t1)
t2 = Time._second_to_time(s1)
print(t1)
print(s1)


#print(Time._time_to_seconds(t1))
print(t2)

t3 = t1+t2



