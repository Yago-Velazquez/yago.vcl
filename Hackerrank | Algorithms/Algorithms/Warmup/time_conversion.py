def timeConversion(s):
    h, m, stime = s.split(":")
    if stime.endswith("PM") and h != "12":
        h = int(h) + 12
        return f"{h}:{m}:{stime.removesuffix('PM')}"
    elif h == "12" and stime.endswith("AM"):
        return f"00:{m}:{stime.removesuffix('AM')}"
    elif h == "12" and stime.endswith("PM"):
        return f"12:{m}:{stime.removesuffix('PM')}"
    else:
        return f"{h}:{m}:{stime.removesuffix('AM')}"
        
if __name__ == '__main__':
    s = input()
    print(timeConversion(s))