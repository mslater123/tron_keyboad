import sys
import json
import random
import maya.cmds as cmds
import math as math
import time as time
from pymel.all import *
import pymel.core as pm

# import pandas as pd

baseTime = 1001

data = {}


def spreadsheet(*args):
    path = cmds.textField(sheetPath, query=True, text=True)
    data = pd.read_excel(r'C:/Users/Mike/Desktop/sheet/assetTracker_v015.xlsx')
    df = pd.DataFrame(data, columns=['Color'])
    print(df)


def getSelection(*args):
    sel = cmds.ls(sl=True)
    return sel


def setings(*args):
    cmds.playbackOptions(min=1001, max=12000)


def set(i, item):
    if i == item:
        i = 0


def setData(i, item, data):
    data.update({item: i})


def readAnim(*args):
    pass


def save(data, filePath):
    with open(filePath, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()


def horn(*args):
    setings()
    time = baseTime
    path = cmds.textField(jsonPath, query=True, text=True)
    gen = cmds.checkBox(genJson, query=True, value=True)
    frames = cmds.intField(frameTotal, query=True, value=True)

    hornLookdevT = cmds.intField(hornLookdevToggle, query=True, value=True)
    hornLookdevS = cmds.intField(hornLookdevStart, query=True, value=True)
    hornLookdevR = cmds.intField(hornLookdevRare, query=True, value=True)
    hornLookdev = []
    for i in range(hornLookdevS, int(hornLookdevR * (hornLookdevT / 100))):
        hornLookdev.append(int(random.random() * hornLookdevT))

    time = baseTime
    for i in range(baseTime, baseTime + (int(frames / hornLookdevT))):
        for a in range(hornLookdevS, hornLookdevT):
            try:
                horn = 'body_varA_0485:horn_lookdev_ctrl'
                cmds.setAttr(horn + '.Horn_Toggle', random.randint(hornLookdevS, a))
                cmds.setKeyframe(horn, at='.Horn_Toggle', t=time)
                time += 1
            except:
                pass


def body(*args):
    setings()
    time = baseTime

    ctrl = 'body_varA_0485:toggle_ctrl'
    items = [
        'body_warpaint_toggle',
        'face_warpaint_toggle',
        'Horn_Type_Toggle',
        'Smokes_Toggle'
    ]

    path = cmds.textField(jsonPath, query=True, text=True)
    gen = cmds.checkBox(genJson, query=True, value=True)
    frames = cmds.intField(frameTotal, query=True, value=True)

    skinT = cmds.intField(skinToggle, query=True, value=True)
    skinS = cmds.intField(skinStart, query=True, value=True)
    skinR = cmds.intField(skinRare, query=True, value=True)
    skin = []
    for i in range(skinS, int(skinR * (skinT / 100))):
        skin.append(int(random.random() * skinT))

    bodyWarpaintT = cmds.intField(bodyWarpaintToggle, query=True, value=True)
    bodyWarpaintS = cmds.intField(bodyWarpaintStart, query=True, value=True)
    bodyWarpaintR = cmds.intField(bodyWarpaintRare, query=True, value=True)
    bodyWarpaint = []
    for i in range(bodyWarpaintS, int(bodyWarpaintR * (bodyWarpaintT / 100))):
        bodyWarpaint.append(int(random.random() * bodyWarpaintT))

    faceWarpaintT = cmds.intField(faceWarpaintToggle, query=True, value=True)
    faceWarpaintS = cmds.intField(faceWarpaintStart, query=True, value=True)
    faceWarpaintR = cmds.intField(faceWarpaintRare, query=True, value=True)
    faceWarpaint = []
    for i in range(faceWarpaintS, int(faceWarpaintR * (faceWarpaintT / 100))):
        faceWarpaint.append(int(random.random() * faceWarpaintT))

    posesT = cmds.intField(posesToggle, query=True, value=True)
    posesS = cmds.intField(posesStart, query=True, value=True)
    posesR = cmds.intField(posesRare, query=True, value=True)
    poses = []
    for i in range(posesS, int(posesR * (posesT / 100))):
        poses.append(int(random.random() * posesT))

    eyeShapeT = cmds.intField(eyeShapeToggle, query=True, value=True)
    eyeShapeS = cmds.intField(eyeShapeStart, query=True, value=True)
    eyeShapeR = cmds.intField(eyeShapeRare, query=True, value=True)
    eyeShape = []
    for i in range(eyeShapeS, int(eyeShapeR * (eyeShapeT / 100))):
        eyeShape.append(int(random.random() * eyeShapeT))

    eyeColorT = cmds.intField(eyeColorToggle, query=True, value=True)
    eyeColorS = cmds.intField(eyeColorStart, query=True, value=True)
    eyeColorR = cmds.intField(eyeColorRare, query=True, value=True)
    eyeColor = []
    for i in range(eyeColorS, int(eyeColorR * (eyeColorT / 100))):
        eyeColor.append(int(random.random() * eyeColorT))

    hornTypeT = cmds.intField(hornTypeToggle, query=True, value=True)
    hornTypeS = cmds.intField(hornTypeStart, query=True, value=True)
    hornTypeR = cmds.intField(hornTypeRare, query=True, value=True)
    hornType = []
    for i in range(hornTypeS, int(hornTypeR * (hornTypeT / 100))):
        hornType.append(int(random.random() * hornTypeT))

    hornLookdevT = cmds.intField(hornLookdevToggle, query=True, value=True)
    hornLookdevS = cmds.intField(hornLookdevStart, query=True, value=True)
    hornLookdevR = cmds.intField(hornLookdevRare, query=True, value=True)
    hornLookdev = []
    for i in range(hornLookdevS, int(hornTypeR * (hornLookdevT / 100))):
        hornLookdev.append(int(random.random() * hornLookdevT))

    smokesT = cmds.intField(smokesToggle, query=True, value=True)
    smokesS = cmds.intField(smokesStart, query=True, value=True)
    smokesR = cmds.intField(smokesRare, query=True, value=True)
    smokes = []
    for i in range(smokesS, int(smokesR * (smokesT / 100))):
        smokes.append(int(random.random() * smokesT))

    time = baseTime
    for i in range(baseTime, baseTime + (int(frames / skinT))):
        for a in range(skinS, skinT):
            cmds.setAttr(ctrl + '.skin_toggle', a)
            cmds.setKeyframe(ctrl, at='.skin_toggle', t=time)
            time += 1

    time = baseTime
    for i in range(baseTime, baseTime + (int(frames / posesT))):
        for a in range(posesS, posesT):
            cmds.setAttr(ctrl + '.poses_toggle', a)
            cmds.setKeyframe(ctrl, at='.poses_toggle', t=time)
            time += 1

    time = baseTime
    for i in range(baseTime, baseTime + (int(frames / eyeShapeT))):
        for a in range(eyeShapeS, eyeShapeT):
            cmds.setAttr(ctrl + '.eye_shape_toggle', a)
            cmds.setKeyframe(ctrl, at='.eye_shape_toggle', t=time)
            time += 1

    time = baseTime
    for i in range(baseTime, baseTime + (int(frames / eyeColorT))):
        for a in range(eyeColorS, eyeColorT):
            cmds.setAttr(ctrl + '.eye_color_toggle', a)
            cmds.setKeyframe(ctrl, at='.eye_color_toggle', t=time)
            time += 1

    time = baseTime
    for i in range(baseTime, baseTime + (int(frames / hornLookdevT))):
        for a in range(hornLookdevS, hornLookdevT):
            try:
                horn = 'body_varA_0485:horn_lookdev_ctrl'
                cmds.setAttr(horn + '.Horn_Toggle', random.randint(hornLookdevS, a))
                cmds.setKeyframe(horn, at='.Horn_Toggle', t=time, inTangentType='stepnext')
                time += 1
            except:
                pass
    time = baseTime

    for i in range(0, 30):
        for b in range(bodyWarpaintS, bodyWarpaintT):
            setData(b, 'bodyWarpaint', data)
            if b in bodyWarpaint:
                continue
            cmds.setAttr(ctrl + '.body_warpaint_toggle', b)

            for c in range(faceWarpaintS, faceWarpaintT):
                set(b, bodyWarpaintT)
                setData(c, 'faceWarpaint', data)
                if c in faceWarpaint:
                    continue
                cmds.setAttr(ctrl + '.face_warpaint_toggle', c)

                for g in range(hornTypeS, hornTypeT):
                    set(b, bodyWarpaintT)
                    set(c, faceWarpaintT)
                    setData(g, 'hornType', data)
                    if g in hornType:
                        continue
                    cmds.setAttr(ctrl + '.Horn_Type_Toggle', g)

                    for h in range(smokesS, smokesT):
                        set(b, bodyWarpaintT)
                        set(c, faceWarpaintT)
                        set(g, hornTypeT)
                        setData(h, 'smokes', data)

                        if h == random.randint(1, 4):
                            h = 0
                        if h == random.randint(1, 2):
                            h = 0
                        if h == random.randint(2, 4):
                            h = 0
                        if h == random.randint(3, 4):
                            h = 0
                        if time == random.randint(baseTime, time):
                            h = 0
                        cmds.setAttr(ctrl + '.Smokes_Toggle', h)

                        # if gen == True:
                        # save(data, path + str(time) + '.json')

                        time += 1
                        for item in items:
                            cmds.setKeyframe(ctrl, at=item, t=time)


def head(*args):
    time = baseTime
    setings()

    ctrl = 'head_toggle:head_toggle'
    items = [
        'Hat_Toggle',
        'Glasses_Toggle'
    ]

    path = cmds.textField(jsonPath, query=True, text=True)
    gen = cmds.checkBox(genJson, query=True, value=True)
    frames = cmds.intField(frameTotal, query=True, value=True)

    hatT = cmds.intField(hatToggle, query=True, value=True)
    hatS = cmds.intField(hatStart, query=True, value=True)
    hatR = cmds.intField(hatRare, query=True, value=True)
    hat = []
    for i in range(hatS, int(hatR * (hatT / 100))):
        hat.append(int(random.random() * hatT))

    hatLookdevT = cmds.intField(hatLookdevToggle, query=True, value=True)
    hatLookdevS = cmds.intField(hatLookdevStart, query=True, value=True)
    hatLookdevR = cmds.intField(hatLookdevRare, query=True, value=True)
    hatLookdev = []
    for i in range(hatS, int(hatLookdevR * (hatLookdevT / 100))):
        hatLookdev.append(int(random.random() * hatLookdevT))

    time = baseTime
    for i in range(baseTime, baseTime + (int(frames / hatLookdevT))):
        for a in range(hatLookdevS, hatLookdevT):
            try:
                cmds.setAttr(ctrl + '.Hat_Lookdev_Toggle', random.randint(hatLookdevS, a))
                cmds.setKeyframe(ctrl, at='.Hat_Lookdev_Toggle', t=time, inTangentType='stepnext')
            except:
                cmds.setKeyframe(ctrl, at='.Glasses_Lookdev_Toggle', t=time, inTangentType='stepnext')
            time += 1

    glassesT = cmds.intField(glassesToggle, query=True, value=True)
    glassesS = cmds.intField(glassesStart, query=True, value=True)
    glassesR = cmds.intField(glassesRare, query=True, value=True)
    glasses = []
    for i in range(glassesS, int(glassesR * (glassesT / 100))):
        glasses.append(int(random.random() * glassesT))

    glassesLookdevT = cmds.intField(glassesLookdevToggle, query=True, value=True)
    glassesLookdevS = cmds.intField(glassesLookdevStart, query=True, value=True)
    glassesLookdevR = cmds.intField(glassesLookdevRare, query=True, value=True)
    glassesLookdev = []
    for i in range(glassesLookdevS, int(glassesLookdevR * (glassesLookdevT / 100))):
        glassesLookdev.append(int(random.random() * glassesLookdevT))

    time = baseTime
    for i in range(baseTime, baseTime + (int(frames / glassesLookdevT))):
        for a in range(glassesLookdevS, glassesLookdevT):
            try:
                cmds.setAttr(ctrl + '.Glasses_Lookdev_Toggle', random.randint(a, hatLookdevT))
                cmds.setKeyframe(ctrl, at='.Glasses_Lookdev_Toggle', t=time, inTangentType='stepnext')
            except:
                cmds.setKeyframe(ctrl, at='.Glasses_Lookdev_Toggle', t=time, inTangentType='stepnext')
            time += 1

    time = baseTime
    for i in range(baseTime, baseTime + 2 + (int(frames / (hatT * glassesT)))):
        for a in range(hatS, hatT):
            try:
                if a in hat:
                    continue

                setData(a, 'hat', data)
                cmds.setAttr(ctrl + '.Hat_Toggle', a)
            except:
                pass

            for c in range(glassesS, glassesT):
                try:
                    set(a, hatT)
                    setData(c, 'glasses', data)
                    if c in glasses:
                        continue

                    if c is 4 and a in (1, 3, 4, 6, 7):
                        c = 0

                    cmds.setAttr(ctrl + '.Glasses_Toggle', c)
                except:
                    pass

                if gen == True:
                    save(data, path + str(time) + '.json')

                time += 1
                for item in items:
                    cmds.setKeyframe(ctrl, at=item, t=time, inTangentType='stepnext')


def neck(*args):
    time = baseTime
    setings()
    ctrl = 'Neck_Toggle:Neck_Toggle'
    items = [
        'Necklace_Toggle',
        'Necklace_Lookdev_Toggle'
    ]

    path = cmds.textField(jsonPath, query=True, text=True)
    gen = cmds.checkBox(genJson, query=True, value=True)
    frames = cmds.intField(frameTotal, query=True, value=True)

    necklaceT = cmds.intField(necklaceToggle, query=True, value=True)
    necklaceS = cmds.intField(necklaceStart, query=True, value=True)
    necklaceR = cmds.intField(necklaceRare, query=True, value=True)
    necklace = []
    for i in range(necklaceS, int(necklaceR * (necklaceT / 100))):
        necklace.append(int(random.random() * necklaceT))

    necklaceLookdevT = cmds.intField(necklaceLookdevToggle, query=True, value=True)
    necklaceLookdevS = cmds.intField(necklaceLookdevStart, query=True, value=True)
    necklaceLookdevR = cmds.intField(necklaceLookdevRare, query=True, value=True)
    necklaceLookdev = []
    for i in range(necklaceLookdevS, int(necklaceLookdevR * (necklaceLookdevT / 100))):
        necklaceLookdev.append(int(random.random() * necklaceLookdevT))

    time = baseTime
    for i in range(baseTime, baseTime + int(frames)):
        for a in range(necklaceS, necklaceT):
            try:
                h = random.randint(a, necklaceT)
                if h == random.randint(1, necklaceT):
                    h = 0
                if h == random.randint(1, necklaceT):
                    h = 0
                if h == random.randint(1, necklaceT):
                    h = 0
                cmds.setAttr(ctrl + '.Necklace_Toggle', int(h))
                cmds.setKeyframe(ctrl, at='.Necklace_Toggle', t=int(time), inTangentType='stepnext')
            except:
                cmds.setKeyframe(ctrl, at='.Necklace_Toggle', t=int(time), inTangentType='stepnext')
            time += 1

    time = baseTime
    for i in range(0, 2700):
        for h in range(necklaceLookdevS, necklaceLookdevT):
            try:
                if h == random.randint(0, necklaceLookdevT):
                    h = 3
                if h == random.randint(0, necklaceLookdevT):
                    h = 2
                cmds.setAttr(ctrl + '.Necklace_Lookdev_Toggle', int(h))
                cmds.setKeyframe(ctrl, at='.Necklace_Lookdev_Toggle', t=int(time), inTangentType='stepnext')
            except:
                cmds.setKeyframe(ctrl, at='.Necklace_Lookdev_Toggle', t=int(time), inTangentType='stepnext')
            time += 1


def jewelry(*args):
    time = baseTime
    setings()
    ctrl = 'Head_Jewelry_Toggle:Head_Jewelry_Toggle'
    items = [
        'Right_Nose_Lookdev_Toggle',
        'Right_Nose_Toggle',
        'Left_Nose_Toggle',
        'Center_Nose_Toggle',
        'Left_Ear_Ring_Toggle',
        'Right_Ear_Ring_Toggle',
        'Left_Nose_lookdev_Toggle',
        'Center_Nose_Lookdev_Toggle',
        'Left_Ear_Ring_Lookdev_Toggle',
        'Right_Ear_Ring_Lookdev_Toggle'
    ]

    path = cmds.textField(jsonPath, query=True, text=True)
    gen = cmds.checkBox(genJson, query=True, value=True)
    frames = cmds.intField(frameTotal, query=True, value=True)

    rightNoseLookdevT = cmds.intField(rightNoseLookdevToggle, query=True, value=True)
    rightNoseLookdevS = cmds.intField(rightNoseLookdevStart, query=True, value=True)
    rightNoseLookdevR = cmds.intField(rightNoseLookdevRare, query=True, value=True)
    rightNoseLookdev = []
    for i in range(rightNoseLookdevR, int(rightNoseLookdevR * (rightNoseLookdevT / 100))):
        rightNoseLookdev.append(int(random.random() * rightNoseLookdevT))

    time = baseTime
    for i in range(0, (int(frames / rightNoseLookdevT) * 2)):
        for a in range(rightNoseLookdevS, rightNoseLookdevT):
            try:
                h = random.randint(a, rightNoseLookdevT)
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                cmds.setAttr(ctrl + '.Right_Nose_Lookdev_Toggle', h)
                cmds.setKeyframe(ctrl, at='.Right_Nose_Lookdev_Toggle', t=time, inTangentType='stepnext')
                time += 1
            except:
                pass

    rightNoseT = cmds.intField(rightNoseToggle, query=True, value=True)
    rightNoseS = cmds.intField(rightNoseStart, query=True, value=True)
    rightNoseR = cmds.intField(rightNoseRare, query=True, value=True)
    rightNose = []
    for i in range(rightNoseS, int(rightNoseR * (rightNoseT / 100))):
        rightNose.append(int(random.random() * rightNoseT))

    time = baseTime
    for i in range(0, (int(frames / rightNoseT) * 2)):
        for a in range(rightNoseS, rightNoseT):
            try:
                h = random.randint(a, rightNoseT)
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                cmds.setAttr(ctrl + '.Right_Nose_Toggle', h)
                cmds.setKeyframe(ctrl, at='.Right_Nose_Toggle', t=time, inTangentType='stepnext')
                time += 1
            except:
                pass

    leftNoseT = cmds.intField(leftNoseToggle, query=True, value=True)
    leftNoseS = cmds.intField(leftNoseStart, query=True, value=True)
    leftNoseR = cmds.intField(leftNoseRare, query=True, value=True)
    leftNose = []
    for i in range(leftNoseS, int(leftNoseR * (leftNoseT / 100))):
        leftNose.append(int(random.random() * leftNoseT))

    time = baseTime
    for i in range(0, (int(frames / leftNoseT) * 2)):
        for a in range(leftNoseS, leftNoseT):
            try:
                h = random.randint(a, leftNoseT)
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                cmds.setAttr(ctrl + '.Left_Nose_Toggle', h)
                cmds.setKeyframe(ctrl, at='.Left_Nose_Toggle', t=time, inTangentType='stepnext')
                time += 1
            except:
                pass

    centerNoseT = cmds.intField(centerNoseToggle, query=True, value=True)
    centerNoseS = cmds.intField(centerNoseStart, query=True, value=True)
    centerNoseR = cmds.intField(centerNoseRare, query=True, value=True)
    centerNose = []
    for i in range(centerNoseS, int(centerNoseR * (centerNoseT / 100))):
        centerNose.append(int(random.random() * centerNoseT))

    time = baseTime
    for i in range(0, (int(frames / centerNoseT) * 3)):
        for a in range(centerNoseS, centerNoseT):
            try:
                h = random.randint(a, centerNoseT)
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                cmds.setAttr(ctrl + '.Center_Nose_Toggle', h)
                cmds.setKeyframe(ctrl, at='.Center_Nose_Toggle', t=time, inTangentType='stepnext')
                time += 1
            except:
                pass

    leftEarRingT = cmds.intField(leftEarRingToggle, query=True, value=True)
    leftEarRingS = cmds.intField(leftEarRingStart, query=True, value=True)
    leftEarRingR = cmds.intField(leftEarRingRare, query=True, value=True)
    leftEarRing = []
    for i in range(leftEarRingS, int(leftEarRingR * (leftEarRingT / 100))):
        leftEarRing.append(int(random.random() * leftEarRingT))

    time = baseTime
    for i in range(0, (int(frames / leftEarRingT) * 2)):
        for b in range(leftEarRingS, leftEarRingT):
            try:
                h = random.randint(b, leftEarRingT)
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, b):
                    h = 0
                cmds.setAttr(ctrl + '.Left_Ear_Ring_Toggle', h)
                cmds.setKeyframe(ctrl, at='.Left_Ear_Ring_Toggle', t=time, inTangentType='stepnext')
                time += 1
            except:
                pass

    rightEarRingT = cmds.intField(rightEarRingToggle, query=True, value=True)
    rightEarRingS = cmds.intField(rightEarRingStart, query=True, value=True)
    rightEarRingR = cmds.intField(rightEarRingRare, query=True, value=True)
    rightEarRing = []
    for i in range(rightEarRingS, int(rightEarRingR * (rightEarRingT / 100))):
        rightEarRing.append(int(random.random() * rightEarRingT))

    time = baseTime
    for i in range(0, (int(frames / rightEarRingT) * 2)):
        for c in range(rightEarRingS, rightEarRingT):
            try:
                h = random.randint(c, rightEarRingT)
                if h == random.randint(1, c):
                    h = 0
                if h == random.randint(1, b):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                cmds.setAttr(ctrl + '.Right_Ear_Ring_Toggle', h)
                cmds.setKeyframe(ctrl, at='.Right_Ear_Ring_Toggle', t=time, inTangentType='stepnext')
                time += 1
            except:
                pass

    leftNoseLookdevT = cmds.intField(leftNoseLookdevToggle, query=True, value=True)
    leftNoseLookdevS = cmds.intField(leftNoseLookdevStart, query=True, value=True)
    leftNoseLookdevR = cmds.intField(leftNoseLookdevRare, query=True, value=True)
    leftNoseLookdev = []
    for i in range(leftNoseLookdevS, int(leftNoseLookdevR * (leftNoseLookdevT / 100))):
        leftNoseLookdev.append(int(random.random() * leftNoseLookdevT))

    time = baseTime
    for i in range(0, (int(frames / leftNoseLookdevT) * 2)):
        for d in range(leftNoseLookdevS, leftNoseLookdevT):
            try:
                h = random.randint(a, leftNoseLookdevT)
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, c):
                    h = 0
                if h == random.randint(1, b):
                    h = 0
                if h == random.randint(1, d):
                    h = 0
                cmds.setAttr(ctrl + '.Left_Nose_lookdev_Toggle', h)
                cmds.setKeyframe(ctrl, at='.Left_Nose_lookdev_Toggle', t=time, inTangentType='stepnext')
                time += 1
            except:
                pass

    centerNoseLookdevT = cmds.intField(centerNoseLookdevToggle, query=True, value=True)
    centerNoseLookdevS = cmds.intField(centerNoseLookdevStart, query=True, value=True)
    centerNoseLookdevR = cmds.intField(centerNoseLookdevRare, query=True, value=True)
    centerNoseLookdev = []
    for i in range(centerNoseLookdevS, int(centerNoseLookdevR * (centerNoseLookdevT / 100))):
        centerNoseLookdev.append(int(random.random() * centerNoseLookdevT))

    time = baseTime
    for i in range(0, (int(frames / centerNoseLookdevT) * 2)):
        for e in range(centerNoseLookdevS, centerNoseLookdevT):
            try:
                h = random.randint(a, centerNoseLookdevT)
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, d):
                    h = 0
                if h == random.randint(1, c):
                    h = 0
                if h == random.randint(1, b):
                    h = 0
                if h == random.randint(1, e):
                    h = 0
                cmds.setAttr(ctrl + '.Center_Nose_Lookdev_Toggle', h)
                cmds.setKeyframe(ctrl, at='.Center_Nose_Lookdev_Toggle', t=time, inTangentType='stepnext')
                time += 1
            except:
                pass

    leftEarRingLookdevT = cmds.intField(leftEarRingLookdevToggle, query=True, value=True)
    leftEarRingLookdevS = cmds.intField(leftEarRingLookdevStart, query=True, value=True)
    leftEarRingLookdevR = cmds.intField(leftEarRingLookdevRare, query=True, value=True)
    leftEarRingLookdev = []
    for i in range(leftEarRingLookdevS, int(leftEarRingLookdevR * (leftEarRingLookdevT / 100))):
        leftEarRingLookdev.append(int(random.random() * leftEarRingLookdevT))

    time = baseTime
    for i in range(0, (int(frames / leftEarRingLookdevT) * 2)):
        for f in range(leftEarRingLookdevS, leftEarRingLookdevT):
            try:
                h = random.randint(f, leftEarRingLookdevT)
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, d):
                    h = 0
                if h == random.randint(1, c):
                    h = 0
                if h == random.randint(1, b):
                    h = 0
                if h == random.randint(1, e):
                    h = 0
                cmds.setAttr(ctrl + '.Left_Ear_Ring_Lookdev_Toggle', h)
                cmds.setKeyframe(ctrl, at='.Left_Ear_Ring_Lookdev_Toggle', t=time, inTangentType='stepnext')
                time += 1
            except:
                pass

    rightEarRingLookdevT = cmds.intField(rightEarRingLookdevToggle, query=True, value=True)
    rightEarRingLookdevS = cmds.intField(rightEarRingLookdevStart, query=True, value=True)
    rightEarRingLookdevR = cmds.intField(rightEarRingLookdevRare, query=True, value=True)
    rightEarRingLookdev = []
    for i in range(rightEarRingLookdevS, int(rightEarRingLookdevR * (rightEarRingLookdevT / 100))):
        rightEarRingLookdev.append(int(random.random() * rightEarRingLookdevT))

    time = baseTime
    for i in range(0, (int(frames / rightEarRingLookdevT) * 2)):
        for g in range(rightEarRingLookdevS, rightEarRingLookdevT):
            try:
                h = random.randint(g, rightEarRingLookdevT)
                if h == random.randint(1, a):
                    h = 0
                if h == random.randint(1, d):
                    h = 0
                if h == random.randint(1, c):
                    h = 0
                if h == random.randint(1, b):
                    h = 0
                if h == random.randint(1, e):
                    h = 0
                cmds.setAttr(ctrl + '.Right_Ear_Ring_Lookdev_Toggle',
                             random.randint(rightEarRingLookdevS, rightEarRingLookdevT))
                cmds.setKeyframe(ctrl, at='.Right_Ear_Ring_Lookdev_Toggle', t=time, inTangentType='stepnext')
                time += 1
            except:
                pass

    '''
    for a in range(rightNoseLookdevS, rightNoseLookdevT):
        if a in rightNoseLookdev:
            continue
        setData(a, 'RightNoseLookdev', data)
        cmds.setAttr(ctrl + '.Right_Nose_Lookdev_Toggle', a)

        for b in range(rightNoseS, rightNoseT):
            set(a, rightNoseLookdevT)
            setData(b, 'RightNose', data)
            if b in rightNose:
                continue
            cmds.setAttr(ctrl + '.Right_Nose_Toggle', b)

            for c in range(leftNoseS, leftNoseT):
                set(a, rightNoseLookdevT)
                set(b, rightNoseT)
                setData(c, 'rightNose', data)
                if c in leftNose:
                    continue
                cmds.setAttr(ctrl + '.Left_Nose_Toggle', c)

                for d in range(centerNoseS, centerNoseT):
                    set(a, rightNoseLookdevT)
                    set(b, rightNoseT)
                    set(c, leftNoseT)
                    setData(d, 'centerNose', data)
                    if d in centerNose:
                        continue
                    cmds.setAttr(ctrl + '.Center_Nose_Toggle', d)

                    for e in range(leftEarRingS, leftEarRingT):
                        set(a, rightNoseLookdevT)
                        set(b, rightNoseT)
                        set(c, leftNoseT)
                        set(d, centerNoseT)
                        setData(e, 'centerNose', data)
                        if e in centerNose:
                            continue
                        cmds.setAttr(ctrl + '.Left_Ear_Ring_Toggle', e)

                        for f in range(rightEarRingS, rightEarRingT):
                            try:
                                set(a, rightNoseLookdevT)
                                set(b, rightNoseT)
                                set(c, leftNoseT)
                                set(d, centerNoseT)
                                set(e, leftEarRingT)
                                setData(f, 'rightEarRing', data)
                                if f in leftEarRing:
                                    continue
                                cmds.setAttr(ctrl + '.Right_Ear_Ring_Toggle', f)
                            except:
                                pass
                            for g in range(leftNoselookdevS, leftNoselookdevT):
                                try:
                                    set(a, rightNoseLookdevT)
                                    set(b, rightNoseT)
                                    set(c, leftNoseT)
                                    set(d, centerNoseT)
                                    set(e, leftEarRingT)
                                    set(f, rightEarRingT)
                                    setData(g, 'leftNoselookdev', data)
                                    if g in leftNoselookdev:
                                        continue                          
                                    cmds.setAttr(ctrl + '.Left_Nose_lookdev_Toggle', g)
                                except:
                                    pass
                                for h in range(centerNoseLookdevS, centerNoseLookdevT):
                                    try:
                                        set(a, rightNoseLookdevT)
                                        set(b, rightNoseT)
                                        set(c, leftNoseT)
                                        set(d, centerNoseT)
                                        set(e, leftEarRingT)
                                        set(f, rightEarRingT)
                                        set(g, leftNoselookdevT)
                                        setData(h, 'centerNoseLookdev', data)
                                        if h in centerNoseLookdev:
                                            continue                          
                                        cmds.setAttr(ctrl + '.Center_Nose_Lookdev_Toggle', h)
                                    except:
                                        pass
                                    for i in range(leftEarRingLookdevS, leftEarRingLookdevT):
                                        try:
                                            set(a, rightNoseLookdevT)
                                            set(b, rightNoseT)
                                            set(c, leftNoseT)
                                            set(d, centerNoseT)
                                            set(e, leftEarRingT)
                                            set(f, rightEarRingT)
                                            set(g, leftNoselookdevT)
                                            set(h, centerNoseLookdevT)
                                            setData(i, 'leftEarRingLookdev', data)
                                            if i in leftEarRingLookdev:
                                                continue                          
                                            cmds.setAttr(ctrl + '.Center_Nose_Lookdev_Toggle', i)
                                        except:
                                            pass
                                        for j in range(rightEarRingLookdevS, rightEarRingLookdevT):
                                            try:
                                                set(a, rightNoseLookdevT)
                                                set(b, rightNoseT)
                                                set(c, leftNoseT)
                                                set(d, centerNoseT)
                                                set(e, leftEarRingT)
                                                set(f, rightEarRingT)
                                                set(g, leftNoselookdevT)
                                                set(h, centerNoseLookdevT)
                                                set(i, leftEarRingLookdevT)
                                                setData(j, 'rightEarRingLookdev', data)
                                                if j in rightEarRingLookdev:
                                                    continue                          
                                                cmds.setAttr(ctrl + '.Center_Nose_Lookdev_Toggle', j)
                                            except:
                                                pass
                                            if gen == True:
                                                save(data, path + str(time) + '.json')

                                            time += 1                   
                                            for item in items:
                                                cmds.setKeyframe(ctrl, at=item, t=time)
    '''


def chest(*args):
    time = baseTime
    setings()

    ctrl = 'chest_toggle:Chest_Shirt_Toggle'
    items = [
        'Chest_Necklace_Toggle',
        'Chest_Necklace_Lookdev_Toggle',
        'Chest_Jacket_Toggle',
        'Chest_Jacket_Lookdev_Toggle'
    ]

    path = cmds.textField(jsonPath, query=True, text=True)
    gen = cmds.checkBox(genJson, query=True, value=True)
    frames = cmds.intField(frameTotal, query=True, value=True)

    chestNecklaceT = cmds.intField(chestNecklaceToggle, query=True, value=True)
    chestNecklaceS = cmds.intField(chestNecklaceStart, query=True, value=True)
    chestNecklaceR = cmds.intField(chestNecklaceRare, query=True, value=True)
    chestNecklace = []
    for i in range(chestNecklaceS, int(chestNecklaceR * (chestNecklaceT / 100))):
        chestNecklace.append(int(random.random() * chestNecklaceT))

    time = baseTime
    for i in range(baseTime, baseTime + (int(frames / chestNecklaceT))):
        for a in range(chestNecklaceS, chestNecklaceT):
            cmds.setAttr(ctrl + '.Chest_Necklace_Toggle', a)
            cmds.setKeyframe(ctrl, at='.Chest_Necklace_Toggle', t=time, inTangentType='stepnext')
            time += 1

    chestNecklaceLookdevT = cmds.intField(chestNecklaceLookdevToggle, query=True, value=True)
    chestNecklaceLookdevS = cmds.intField(chestNecklaceLookdevStart, query=True, value=True)
    chestNecklaceLookdevR = cmds.intField(chestNecklaceLookdevRare, query=True, value=True)
    chestNecklaceLookdev = []
    for i in range(chestNecklaceLookdevS, int(chestNecklaceLookdevR * (chestNecklaceLookdevT / 100))):
        chestNecklaceLookdev.append(int(random.random() * chestNecklaceLookdevT))

    time = baseTime
    for i in range(baseTime, baseTime + (int(frames / chestNecklaceLookdevT))):
        for a in range(chestNecklaceLookdevS, chestNecklaceLookdevT):
            cmds.setAttr(ctrl + '.Chest_Necklace_Lookdev_Toggle', a)
            cmds.setKeyframe(ctrl, at='.Chest_Necklace_Lookdev_Toggle', t=time, inTangentType='stepnext')
            time += 1

    chestJacketT = cmds.intField(chestJacketToggle, query=True, value=True)
    chestJacketS = cmds.intField(chestJacketStart, query=True, value=True)
    chestJacketR = cmds.intField(chestJacketRare, query=True, value=True)
    chestJacket = []
    for i in range(chestJacketS, int(chestJacketR * (chestJacketT / 100))):
        chestJacket.append(int(random.random() * chestJacketT))

    time = baseTime
    for i in range(baseTime, baseTime + (int(frames / chestJacketT))):
        for a in range(chestJacketS, chestJacketT):
            cmds.setAttr(ctrl + '.Chest_Jacket_Toggle', a)
            cmds.setKeyframe(ctrl, at='.Chest_Jacket_Toggle', t=time, inTangentType='stepnext')
            time += 1

    chestJacketLookdevT = cmds.intField(chestJacketLookdevToggle, query=True, value=True)
    chestJacketLookdevS = cmds.intField(chestJacketLookdevStart, query=True, value=True)
    chestJacketLookdevR = cmds.intField(chestJacketLookdevRare, query=True, value=True)
    chestJacketLookdev = []
    for i in range(chestJacketLookdevS, int(chestJacketLookdevR * (chestJacketLookdevT / 100))):
        chestJacketLookdev.append(int(random.random() * chestJacketLookdevT))

    time = baseTime
    for i in range(baseTime, baseTime + (int(frames / chestJacketLookdevT))):
        for a in range(chestJacketLookdevS, chestJacketLookdevT):
            cmds.setAttr(ctrl + '.Chest_Jacket_Lookdev_Toggle', a)
            cmds.setKeyframe(ctrl, at='.Chest_Jacket_Lookdev_Toggle', t=time, inTangentType='stepnext')
            time += 1
    '''
    for a in range(chestNecklaceS, chestNecklaceT):
        try:
            if a in chestNecklace:
                continue
            setData(a, 'chestNecklace', data)
            cmds.setAttr(ctrl + '.Chest_Necklace_Toggle', a)
        except:
            pass
        for b in range(chestNecklaceLookdevS, chestNecklaceLookdevT):
            try:
                set(a, chestNecklaceT)
                setData(b, 'hat_toggle', data)
                if b in bodyWarpaint:
                    continue
                cmds.setAttr(ctrl + '.Chest_Necklace_Lookdev_Toggle', b)
            except:
                pass
            for c in range(chestJacketS, chestJacketT):
                try:
                    set(a, chestNecklaceT)
                    set(b, chestNecklaceLookdevT)
                    setData(c, 'chestJacket', data)
                    if c in chestJacket:
                        continue
                    cmds.setAttr(ctrl + '.Chest_Jacket_Toggle', c)
                except:
                    pass
                for d in range(chestJacketLookdevS, chestJacketLookdevT):
                    try:
                        set(a, chestNecklaceT)
                        set(b, chestNecklaceLookdevT)
                        set(c, chestJacketT)
                        setData(d, 'chestJacketLookdev', data)
                        if d in chestNecklace:
                            continue
                        cmds.setAttr(ctrl + '.Chest_Jacket_Lookdev_Toggle', d)
                    except:
                        pass                             
                    if gen == True:
                        save(data, path + str(time) + '.json')

                    time += 1
                    for item in items:
                        cmds.setKeyframe(ctrl, at=item, t=time, inTangentType='stepnext')
    '''


# Make window
window = cmds.window(title='Rhino Tool', iconName='Short Name', widthHeight=(302, 852))

cmds.rowColumnLayout(numberOfColumns=4)

cmds.text(label='json path', w=50)
genJson = cmds.checkBox(w=50, value=0, editable=True)
cmds.text(label='frames', w=50)
frameTotal = cmds.intField(w=50, value=12000, editable=True)

jsonPath = cmds.textField(w=50, text='C:/Users/Mike/Desktop/test/', editable=True)
cmds.text(label='start', w=50)
cmds.text(label='end', w=50)
cmds.text(label='rarity', w=50)

# Body
cmds.text(label='Skin Toggle', w=150)
skinStart = cmds.intField(w=50, value=0, editable=True)
skinToggle = cmds.intField(w=50, value=6, editable=True)
skinRare = cmds.intField(w=50, value=0, editable=True)

cmds.text(label='Body Warpaint Toggle', w=150)
bodyWarpaintStart = cmds.intField(w=50, value=0, editable=True)
bodyWarpaintToggle = cmds.intField(w=50, value=5, editable=True)
bodyWarpaintRare = cmds.intField(w=50, value=0, editable=True)

cmds.text(label='Face Warpaint Toggle', w=150)
faceWarpaintStart = cmds.intField(w=50, value=0, editable=True)
faceWarpaintToggle = cmds.intField(w=50, value=6, editable=True)
faceWarpaintRare = cmds.intField(w=50, value=0, editable=True)

cmds.text(label='Poses Toggle', w=150)
posesStart = cmds.intField(w=50, value=0, editable=True)
posesToggle = cmds.intField(w=50, value=7, editable=True)
posesRare = cmds.intField(w=50, value=0, editable=True)

cmds.text(label='Eye Shape Toggle', w=150)
eyeShapeStart = cmds.intField(w=50, value=0, editable=True)
eyeShapeToggle = cmds.intField(w=50, value=3, editable=True)
eyeShapeRare = cmds.intField(w=50, value=0, editable=True)

cmds.text(label='Eye Color Toggle', w=150)
eyeColorStart = cmds.intField(w=50, value=0, editable=True)
eyeColorToggle = cmds.intField(w=50, value=4, editable=True)
eyeColorRare = cmds.intField(w=50, value=0, editable=True)

cmds.text(label='Horn Type Toggle', w=150)
hornTypeStart = cmds.intField(w=50, value=0, editable=True)
hornTypeToggle = cmds.intField(w=50, value=5, editable=True)
hornTypeRare = cmds.intField(w=50, value=0, editable=True)

cmds.text(label='Smokes Toggle', w=150)
smokesStart = cmds.intField(w=50, value=0, editable=True)
smokesToggle = cmds.intField(w=50, value=4, editable=True)
smokesRare = cmds.intField(w=50, value=0, editable=True)

cmds.button('Body', w=150, h=35, align='center', backgroundColor=[0.1, 0.2, 0.3], c=body)
cmds.text(label='')
cmds.text(label='')
cmds.text(label='')

# Head
cmds.text(label='Hat Toggle', w=150)
hatStart = cmds.intField(w=50, value=0, editable=True)
hatToggle = cmds.intField(w=50, value=9, editable=True)
hatRare = cmds.intField(w=50, value=0, editable=True)

cmds.text(label='Hat Lookdev Toggle', w=150)
hatLookdevStart = cmds.intField(w=50, value=0, editable=True)
hatLookdevToggle = cmds.intField(w=50, value=4, editable=True)
hatLookdevRare = cmds.intField(w=50, value=0, editable=True)

cmds.text(label='Glasses Toggle', w=150)
glassesStart = cmds.intField(w=50, value=0, editable=True)
glassesToggle = cmds.intField(w=50, value=7, editable=True)
glassesRare = cmds.intField(w=50, value=0, editable=True)

cmds.text(label='Glasses Lookdev Toggle', w=150)
glassesLookdevStart = cmds.intField(w=50, value=0, editable=True)
glassesLookdevToggle = cmds.intField(w=50, value=4, editable=True)
glassesLookdevRare = cmds.intField(w=50, value=0, editable=True)

cmds.button('Head', w=150, h=35, align='center', backgroundColor=[0.3, 0.1, 0.1], c=head)
cmds.text(label='')
cmds.text(label='')
cmds.text(label='')

# Neck
cmds.text(label='Necklace Toggle', w=150)
necklaceStart = cmds.intField(w=50, value=0, editable=True)
necklaceToggle = cmds.intField(w=50, value=7, editable=True)
necklaceRare = cmds.intField(w=50, value=0, editable=True)

cmds.text(label='Necklace Lookdev Toggle', w=150)
necklaceLookdevStart = cmds.intField(w=50, value=0, editable=True)
necklaceLookdevToggle = cmds.intField(w=50, value=4, editable=True)
necklaceLookdevRare = cmds.intField(w=50, value=0, editable=True)

cmds.button('Neck', w=150, h=35, align='center', backgroundColor=[0.8, 0.1, 0.3], c=neck)
cmds.text(label='')
cmds.text(label='')
cmds.text(label='')

# Jewelry
cmds.text(label='Right Nose Lookdev Toggle', w=150)
rightNoseLookdevStart = cmds.intField(w=50, value=0, editable=True)
rightNoseLookdevToggle = cmds.intField(w=50, value=4, editable=True)
rightNoseLookdevRare = cmds.intField(w=50, value=30, editable=True)

cmds.text(label='Right Nose Toggle', w=150)
rightNoseStart = cmds.intField(w=50, value=0, editable=True)
rightNoseToggle = cmds.intField(w=50, value=4, editable=True)
rightNoseRare = cmds.intField(w=50, value=30, editable=True)

cmds.text(label='Left Nose Toggle', w=150)
leftNoseStart = cmds.intField(w=50, value=0, editable=True)
leftNoseToggle = cmds.intField(w=50, value=4, editable=True)
leftNoseRare = cmds.intField(w=50, value=30, editable=True)

cmds.text(label='Center Nose Toggle', w=150)
centerNoseStart = cmds.intField(w=50, value=0, editable=True)
centerNoseToggle = cmds.intField(w=50, value=3, editable=True)
centerNoseRare = cmds.intField(w=50, value=30, editable=True)

cmds.text(label='Left Ear Ring Toggle', w=150)
leftEarRingStart = cmds.intField(w=50, value=0, editable=True)
leftEarRingToggle = cmds.intField(w=50, value=5, editable=True)
leftEarRingRare = cmds.intField(w=50, value=30, editable=True)

cmds.text(label='Right Ear Ring Toggle', w=150)
rightEarRingStart = cmds.intField(w=50, value=0, editable=True)
rightEarRingToggle = cmds.intField(w=50, value=5, editable=True)
rightEarRingRare = cmds.intField(w=50, value=30, editable=True)

cmds.text(label='Left Nose lookdev Toggle', w=150)
leftNoseLookdevStart = cmds.intField(w=50, value=0, editable=True)
leftNoseLookdevToggle = cmds.intField(w=50, value=4, editable=True)
leftNoseLookdevRare = cmds.intField(w=50, value=30, editable=True)

cmds.text(label='Center Nose Lookdev Toggle', w=150)
centerNoseLookdevStart = cmds.intField(w=50, value=0, editable=True)
centerNoseLookdevToggle = cmds.intField(w=50, value=4, editable=True)
centerNoseLookdevRare = cmds.intField(w=50, value=30, editable=True)

cmds.text(label='Left Ear Ring Lookdev Toggle', w=150)
leftEarRingLookdevStart = cmds.intField(w=50, value=0, editable=True)
leftEarRingLookdevToggle = cmds.intField(w=50, value=4, editable=True)
leftEarRingLookdevRare = cmds.intField(w=50, value=30, editable=True)

cmds.text(label='Right Ear Ring Lookdev Toggle', w=150)
rightEarRingLookdevStart = cmds.intField(w=50, value=0, editable=True)
rightEarRingLookdevToggle = cmds.intField(w=50, value=4, editable=True)
rightEarRingLookdevRare = cmds.intField(w=50, value=30, editable=True)

cmds.button('Jewelry', w=150, h=35, align='center', backgroundColor=[0.3, 0.5, 0.3], c=jewelry)
cmds.text(label='')
cmds.text(label='')
cmds.text(label='')

# Chest
cmds.text(label='Chest Necklace Toggle', w=150)
chestNecklaceStart = cmds.intField(w=50, value=0, editable=True)
chestNecklaceToggle = cmds.intField(w=50, value=5, editable=True)
chestNecklaceRare = cmds.intField(w=50, value=30, editable=True)

cmds.text(label='Chest Necklace Lookdev Toggle', w=150)
chestNecklaceLookdevStart = cmds.intField(w=50, value=0, editable=True)
chestNecklaceLookdevToggle = cmds.intField(w=50, value=4, editable=True)
chestNecklaceLookdevRare = cmds.intField(w=50, value=30, editable=True)

cmds.text(label='Chest Jacket Toggle', w=150)
chestJacketStart = cmds.intField(w=50, value=1, editable=True)
chestJacketToggle = cmds.intField(w=50, value=13, editable=True)
chestJacketRare = cmds.intField(w=50, value=30, editable=True)

cmds.text(label='Chest Jacket Lookdev Toggle', w=150)
chestJacketLookdevStart = cmds.intField(w=50, value=0, editable=True)
chestJacketLookdevToggle = cmds.intField(w=50, value=4, editable=True)
chestJacketLookdevRare = cmds.intField(w=50, value=30, editable=True)

cmds.button('Chest', w=150, h=35, align='center', backgroundColor=[0.1, 0.6, 0.1], c=chest)
cmds.text(label='')
cmds.text(label='')
cmds.text(label='')

cmds.text(label='Horn Lookdev Toggle', w=150)
hornLookdevStart = cmds.intField(w=50, value=0, editable=True)
hornLookdevToggle = cmds.intField(w=50, value=5, editable=True)
hornLookdevRare = cmds.intField(w=50, value=0, editable=True)

cmds.button('Horn', w=150, h=35, align='center', backgroundColor=[0.1, 0.6, 0.1], c=horn)
cmds.text(label='')
cmds.text(label='')
cmds.text(label='')
# sheetPath = cmds.textField(w=50, text=r'C:/Users/Mike/Desktop/sheet/assetTracker_v015.xlsx', editable=True)
# cmds.button('Spreadsheet', w=150, h=35, align='center', backgroundColor=[0.1, 0.6, 0.1], c=spreadsheet)
# cmds.setParent('..')
cmds.showWindow(window)