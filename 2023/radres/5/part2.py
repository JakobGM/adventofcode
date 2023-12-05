from helpers import *
with open("input.txt", "r") as f:
    out = f.read()

lines = out.splitlines()
# forstart_range line in lines:
#     print(line)

seeds = [2494933545, 159314859, 4045092792, 172620202, 928898138, 554061882, 2740120981, 81327018, 2031777983, 63513119, 2871914181, 270575980, 2200250633, 216481794, 3289604059, 25147787, 3472625834, 10030240, 260990830, 232636388]


seed_to_soil = []
for line in """3272284283 2724782980 1022683013
138187491 4195038636 99928660
2359623759 797621236 127984779
662451929 2224466386 266466256
928918185 714355413 83265823
1012184008 3891516474 303522162
3063776460 1098322140 208507823
2194238166 1306829963 50525692
357106588 2091837170 132629216
2244763858 2490932642 114859901
2050187685 3747465993 144050481
489735804 925606015 172716125
2487608538 138187491 576167922
238116151 2605792543 118990437
1315706170 1357355655 734481515""".splitlines():

    seed_to_soil.append(extract_integers_from_text(line))

soil_to_fert = []
for line in """4265669768 2142212766 29297528
2030756625 2171510294 69737894
3038084234 3411621093 262803613
2410534622 3266307064 145314029
2667304792 2241248188 370779442
2100494519 3921619167 310040103
3611390334 2612027630 654279434
2555848651 2030756625 111456141
733063720 869238953 195075492
3300887847 4231659270 63308026
3364195873 3674424706 247194461
928139212 733063720 136175233""".splitlines():
    soil_to_fert.append(extract_integers_from_text(line))



fert_to_wat = []
for line in """0 772139976 154052576
909628165 428370542 51644443
3172969725 4109584032 185383264
1116931128 1046566515 14194115
223777814 10055892 255169216
2512535520 1229983026 60386000
3109777744 3899207072 16374329
4030761870 3829858282 12540292
828135093 718323602 53816374
2358450176 2554590817 154085344
3126152073 3152512175 46817652
4043302162 3842398574 56808498
3694349069 3493296400 336412801
770911368 661099877 57223725
3574254366 3032417472 120094703
2689829955 2124052738 139986329
3358352989 1925653441 3542661
154052576 1060760630 69725238
3460616091 3829709201 149081
881951467 480014985 9494517
1777535488 3915581401 135358522
2829816284 1290369026 84715328
478947030 489509502 171590375
2686813330 1226966401 3016625
3361895650 3199329827 98720441
1226966401 1375084354 550569087
3515610257 4050939923 58644109
650537405 926192552 120373963
4100110660 1929196102 194856636
1912894010 2708676161 323741311
3460765172 2264039067 54845085
898932898 0 10055892
891445984 265225108 7486914
2914531612 3298050268 195246132
2572921520 2318884152 113891810
961272608 272712022 155658520
908988790 1130485868 639375
2236635321 2432775962 121814855""".splitlines():
    fert_to_wat.append(extract_integers_from_text(line))

wat_to_lig = []
for line in """2821176146 2286693663 106119314
3822234587 2463633329 180779736
1725724347 2842879211 104224606
3308097155 4172728180 122239116
3299768179 2834550235 8328976
525232540 357109336 38255672
751267412 803626289 867213460
2181067610 2392812977 70820352
2251887962 2644413065 134698828
3430336271 3994876090 163182805
357109336 395365008 62712446
3646455511 2158365540 128328123
3084834769 2947103817 214933410
1618480872 3954660777 40215313
1673365470 751267412 52358877
2927295460 3797121468 157539309
2386586790 1723776184 434589356
3774783634 2779111893 47450953
4003014323 3162037227 291952973
419821782 458077454 105410758
3593519076 1670839749 52936435
1658696185 4158058895 14669285
2173080221 2826562846 7987389
1829948953 3453990200 343131268""".splitlines():
    wat_to_lig.append(extract_integers_from_text(line))

lig_to_tem = []
for line in """457330729 4090205185 204762111
2982196520 3401667644 30193953
2238727594 3778270640 263367024
2540710222 1921368253 380651678
2224576409 4041637664 14151185
1803946096 1170025919 125923944
947791690 3069412788 65888847
3354708582 3597834895 180435745
1173448701 516297801 630497395
4079424710 2899828022 88028778
1929870040 1295949863 294706369
928458849 495946333 19332841
3145865299 515279174 1018627
3071616223 2825578946 74249076
3012390473 3431861597 52676537
0 156654134 174053721
1013680537 1590656232 159768164
2502094618 457330729 38615604
4167453488 3484538134 113296761
4058703342 3048691420 20721368
3146883926 1750424396 164394644
662092840 3135301635 266366009
174053721 0 156654134
4280750249 4055788849 14217047
3311278570 1146795196 23230723
3334509293 4070005896 20199289
3535144327 2302019931 523559015
3065067010 1914819040 6549213
2921361900 2987856800 60834620""".splitlines():
    lig_to_tem.append(extract_integers_from_text(line))


tem_to_hum = []
for line in """19014508 1616728169 261978440
479364011 879054632 183139707
3422279791 4197415651 97551645
2947838505 2859883311 474441286
3922771609 3441941550 130194267
1538347549 1285663854 77335299
4074125861 3334324597 17231539
2692139672 3923798143 165313419
3867887507 3572135817 45827004
4091357400 2695950683 148956394
280992948 874337342 4717290
3585981058 4137845928 59569723
1194193608 267159640 344153941
3645550781 2226309992 39998882
2606341883 3617962821 85797789
2452453972 3769910232 153887911
4279991062 2844907077 14976234
4240313794 4089111562 39677268
285710238 0 193653773
662503718 1585706204 31021965
4052965876 2266308874 21159985
2226309992 2287468859 226143980
0 248145132 19014508
3685549663 2513612839 182337844
2857453091 3351556136 90385414
1139702249 193653773 54491359
3913714511 4128788830 9057098
916232734 1062194339 223469515
1615682848 611313581 263023761
693525683 1362999153 222707051
3519831436 3703760610 66149622""".splitlines():
    tem_to_hum.append(extract_integers_from_text(line))


hum_to_loc = []
for line in """3722067319 3568864729 46052123
761939125 1263883488 182519766
3952597071 3400791743 168072986
1928058 204065059 218803536
1797120632 863951513 248903371
3409129274 3614916852 109595510
0 1261955430 1928058
3854871689 2940386871 97725382
3518724784 3898809601 159455982
220731594 1446403254 100124613
944458891 1813379640 207908225
3194065032 4058265583 117770911
3059317673 3222157831 134747359
3678180766 3356905190 43886553
3375153977 3124864500 33975297
2940386871 4176036494 118930802
1152367116 2021287865 24736138
3311835943 3158839797 63318034
320856207 422868595 441082918
1593055573 0 204065059
4120670057 3724512362 174297239
1177103254 1112854884 149100546
1326203800 1546527867 266851773
3768119442 3038112253 86752247""".splitlines():
    hum_to_loc.append(extract_integers_from_text(line))


def find_intersection(range1, range2):
    start = max(range1.start, range2.start)
    end = min(range1.stop, range2.stop)

    if start < end:
        return range(start, end)
    else:
        return None

def shift_range(input_range, shift_amount):
    new_start = input_range.start + shift_amount
    new_stop = input_range.stop + shift_amount
    return range(new_start, new_stop)

def find_difference(range1, range2):
    if range1.start >= range2.stop or range1.stop <= range2.start:
        return [range1]
    elif range1.start >= range2.start and range1.stop <= range2.stop:
        return []
    elif range1.start < range2.start and range1.stop <= range2.stop:
        return [range(range1.start, range2.start)]
    elif range1.start >= range2.start and range1.stop > range2.stop:
        return [range(range2.stop, range1.stop)]
    else:
        return [range(range1.start, range2.start), range(range2.stop, range1.stop)]

def merge_ranges(ranges):
    if not ranges:
        return []

    # Sort the ranges by their start values
    sorted_ranges = sorted(ranges, key=lambda x: x.start)
    
    merged_ranges = [sorted_ranges[0]]

    for current_range in sorted_ranges[1:]:
        last_merged_range = merged_ranges[-1]

        # Check if the current range overlaps with the last merged range
        if current_range.start <= last_merged_range.stop:
            # Merge the current range with the last merged range
            merged_ranges[-1] = range(last_merged_range.start, max(last_merged_range.stop, current_range.stop))
        else:
            # Add the current range to the merged list
            merged_ranges.append(current_range)

    return merged_ranges

# seeds = [79,14,55,13]
# seed_to_soil = [(50, 98, 2), (52, 50, 48)]
# soil_to_fert = [(0, 15, 37), (37, 52, 2), (39, 0, 15)]
# fert_to_wat = [(49, 53, 8), (0, 11, 42), (42, 0, 7), (57, 7, 4)]
# wat_to_lig = [(88, 18, 7), (18, 25, 70)]
# lig_to_tem =[(45, 77, 23), (81, 45, 19), (68, 64, 13)]
# tem_to_hum = [(0, 69, 1), (1, 0, 69)]
# hum_to_loc = [(60, 56, 37), (56, 93, 4)]

seed_ranges = []
i = 0
while i < len(seeds)-1:
    ss, sl = seeds[i], seeds[i+1]
    seed_ranges.append(range(ss,ss+sl))
    i+=2

start_range = seed_ranges
end_range = []
source_ranges = []
for sr in start_range:
    for vec in seed_to_soil:
        i,j,k = vec
        source_range, dest_range = (range(j,j+k), range(i,i+k))
        source_ranges.append(source_range)
        inter = find_intersection(sr, source_range)
        if inter:
            end_range.append(shift_range(inter, i-j))

    diffs = set()
    diffs.add(sr)
    procd_diffs = set()
    result_diff = []
    while diffs:
        diff = diffs.pop()
        no_inter = True
        for sour_r in source_ranges:
            new_diffs = find_difference(diff, sour_r)
            no_inter = no_inter and len(new_diffs) == 1 and new_diffs[0] == diff
            for newd in new_diffs:
                if newd not in procd_diffs:
                    diffs.add(newd)
        if no_inter:
            result_diff.append(diff)
        procd_diffs.add(diff)

    for r in merge_ranges(result_diff):
        end_range.append(r)
end_range = merge_ranges(end_range)


start_range = end_range
end_range = []
source_ranges = []
for sr in start_range:
    for vec in soil_to_fert:
        i,j,k = vec
        source_range, dest_range = (range(j,j+k), range(i,i+k))
        source_ranges.append(source_range)
        inter = find_intersection(sr, source_range)
        if inter:
            end_range.append(shift_range(inter, i-j))

    diffs = set()
    diffs.add(sr)
    procd_diffs = set()
    result_diff = []
    while diffs:
        diff = diffs.pop()
        no_inter = True
        for sour_r in source_ranges:
            new_diffs = find_difference(diff, sour_r)
            no_inter = no_inter and len(new_diffs) == 1 and new_diffs[0] == diff
            for newd in new_diffs:
                if newd not in procd_diffs:
                    diffs.add(newd)
        if no_inter:
            result_diff.append(diff)
        procd_diffs.add(diff)


    for r in merge_ranges(result_diff):
        end_range.append(r)
end_range = merge_ranges(end_range)


start_range = end_range
end_range = []
source_ranges = []
for sr in start_range:
    for vec in fert_to_wat:
        i,j,k = vec
        source_range, dest_range = (range(j,j+k), range(i,i+k))
        source_ranges.append(source_range)
        inter = find_intersection(sr, source_range)
        if inter:
            end_range.append(shift_range(inter, i-j))

    diffs = set()
    diffs.add(sr)
    procd_diffs = set()
    result_diff = []
    while diffs:
        diff = diffs.pop()
        no_inter = True
        for sour_r in source_ranges:
            new_diffs = find_difference(diff, sour_r)
            no_inter = no_inter and len(new_diffs) == 1 and new_diffs[0] == diff
            for newd in new_diffs:
                if newd not in procd_diffs:
                    diffs.add(newd)
        if no_inter:
            result_diff.append(diff)
        procd_diffs.add(diff)


    for r in merge_ranges(result_diff):
        end_range.append(r)
end_range = merge_ranges(end_range)

start_range = end_range
end_range = []
source_ranges = []
for sr in start_range:
    for vec in wat_to_lig:
        i,j,k = vec
        source_range, dest_range = (range(j,j+k), range(i,i+k))
        source_ranges.append(source_range)
        inter = find_intersection(sr, source_range)
        if inter:
            end_range.append(shift_range(inter, i-j))

    diffs = set()
    diffs.add(sr)
    procd_diffs = set()
    result_diff = []
    while diffs:
        diff = diffs.pop()
        no_inter = True
        for sour_r in source_ranges:
            new_diffs = find_difference(diff, sour_r)
            no_inter = no_inter and len(new_diffs) == 1 and new_diffs[0] == diff
            for newd in new_diffs:
                if newd not in procd_diffs:
                    diffs.add(newd)
        if no_inter:
            result_diff.append(diff)
        procd_diffs.add(diff)


    for r in merge_ranges(result_diff):
        end_range.append(r)
end_range = merge_ranges(end_range)

start_range = end_range
end_range = []
source_ranges = []
for sr in start_range:
    for vec in lig_to_tem:
        i,j,k = vec
        source_range, dest_range = (range(j,j+k), range(i,i+k))
        source_ranges.append(source_range)
        inter = find_intersection(sr, source_range)
        if inter:
            end_range.append(shift_range(inter, i-j))

    diffs = set()
    diffs.add(sr)
    procd_diffs = set()
    result_diff = []
    while diffs:
        diff = diffs.pop()
        no_inter = True
        for sour_r in source_ranges:
            new_diffs = find_difference(diff, sour_r)
            no_inter = no_inter and len(new_diffs) == 1 and new_diffs[0] == diff
            for newd in new_diffs:
                if newd not in procd_diffs:
                    diffs.add(newd)
        if no_inter:
            result_diff.append(diff)
        procd_diffs.add(diff)


    for r in merge_ranges(result_diff):
        end_range.append(r)
end_range = merge_ranges(end_range)


start_range = end_range
end_range = []
source_ranges = []
for sr in start_range:
    for vec in tem_to_hum:
        i,j,k = vec
        source_range, dest_range = (range(j,j+k), range(i,i+k))
        source_ranges.append(source_range)
        inter = find_intersection(sr, source_range)
        if inter:
            end_range.append(shift_range(inter, i-j))

    diffs = set()
    diffs.add(sr)
    procd_diffs = set()
    result_diff = []
    while diffs:
        diff = diffs.pop()
        no_inter = True
        for sour_r in source_ranges:
            new_diffs = find_difference(diff, sour_r)
            no_inter = no_inter and len(new_diffs) == 1 and new_diffs[0] == diff
            for newd in new_diffs:
                if newd not in procd_diffs:
                    diffs.add(newd)
        if no_inter:
            result_diff.append(diff)
        procd_diffs.add(diff)


    for r in merge_ranges(result_diff):
        end_range.append(r)
end_range = merge_ranges(end_range)



start_range = end_range
end_range = []
source_ranges = []
for sr in start_range:
    for vec in hum_to_loc:
        i,j,k = vec
        source_range, dest_range = (range(j,j+k), range(i,i+k))
        source_ranges.append(source_range)
        inter = find_intersection(sr, source_range)
        if inter:
            end_range.append(shift_range(inter, i-j))

    diffs = set()
    diffs.add(sr)
    procd_diffs = set()
    result_diff = []
    while diffs:
        diff = diffs.pop()
        no_inter = True
        for sour_r in source_ranges:
            new_diffs = find_difference(diff, sour_r)
            no_inter = no_inter and len(new_diffs) == 1 and new_diffs[0] == diff
            for newd in new_diffs:
                if newd not in procd_diffs:
                    diffs.add(newd)
        if no_inter:
            result_diff.append(diff)
        procd_diffs.add(diff)


    for r in merge_ranges(result_diff):
        end_range.append(r)
end_range = merge_ranges(end_range)

print(end_range)

mini = 999999999999999999
for loc in end_range:
    mini = min(mini, min(loc.start, loc.stop-1))
print(mini)
