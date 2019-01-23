# -*- coding: utf-8 -*-
from mafuLib.linepy import *
import time
from random import choice
print("nk_01=LINE("+'"'+ str(nk_01.authToken)+'"'+")")
print("nk_02=LINE("+'"'+ str(nk_02.authToken)+'"'+")")
print("nk_03=LINE("+'"'+ str(nk_03.authToken)+'"'+")")
print("nk_04=LINE("+'"'+ str(nk_04.authToken)+'"'+")")
print("nk_05=LINE("+'"'+ str(nk_05.authToken)+'"'+")")
print("nk_06=LINE("+'"'+ str(nk_06.authToken)+'"'+")")
print("nk_07=LINE("+'"'+ str(nk_07.authToken)+'"'+")")
print("nk_08=LINE("+'"'+ str(nk_08.authToken)+'"'+")")
nks=[]#参加nekosuke
lv_list=[]#生存nekosuke
allnks=[nk_01,nk_02,nk_03,nk_04,nk_05,nk_06,nk_07,nk_08]


mid_01=nk_01.getProfile().mid
mid_02=nk_02.getProfile().mid
mid_03=nk_03.getProfile().mid
mid_04=nk_04.getProfile().mid
mid_05=nk_05.getProfile().mid
mid_06=nk_06.getProfile().mid
mid_07=nk_07.getProfile().mid
mid_08=nk_08.getProfile().mid



nkids=[mid_01,mid_02,mid_03,mid_04,mid_05,mid_06,mid_07,mid_08]

B_list=[]
B_listName=[]
G_list=[]
G_listName=[]
G_members=[]
users=[]
Reception=[]
G_URL=[]

flag=[]


while True:
    try:
        ops_nk01=nk_01.poll.fetchOperations(nk_01.revision,50)


    except:
        continue

    if ops_nk01!=None:
            for op in ops_nk01:
                try:
                    if op.type==0:
                        pass
                    if op.type==10:#I change groupname
                        pass
                    if op.type==11:#A member changes groupname
                            G=nk_01.getGroup(op.param1)
                            gid=G.id
                            n=G_list.index(gid)#グループ番号
                            old=G_listName[n]
                            cn=nk_01.getContact(op.param2)
                            nk_01.sendMessage(op.param1,cn.displayName+"さんがグループ名を"+old+"から"+G.name+"に変更しました。")
                            G_listName[n]=G.name
                    if op.type==13:
                        if op.param3==mid_01:
                            nk_01.acceptGroupInvitation(op.param1)
                        elif op.param3 in B_list:
                            B_list.append(op.param2)
                            cnt=nk_01.getContact(op.param2)
                            B_listName.append(cnt.displayName)
                            nk_01.cancelGroupInvitation(op.param1,[op.param3])
                            nk_01.kickoutFromGroup(op.param1,[op.param2])
                    if op.type==15:
                        if op.param2 in nkids:
                            n=nkids.index(op.param2)
                            if n==1:
                                nks.remove(nk_02)
                            elif n==2:
                                nks.remove(nk_03)
                            elif n==3:
                                nks.remove(nk_04)
                            elif n==4:
                                nks.remove(nk_05)
                            elif n==5:
                                nks.remove(nk_06)
                            elif n==6:
                                nks.remove(nk_07)
                            elif n==7:
                                nks.remove(nk_08)

                    if op.type==16:
                        G=nk_01.getGroup(op.param1)
                        G_list.append(G.id)
                        G_listName.append(G.name)
                        Reception.append("on")
                        flag.append(0)
                        T=nk_01.reissueGroupTicket(op.param1)
                        G_URL.append(T)
                        memid=[i.mid for i in G.members]
                        user=""
                        memid.remove(mid_01)
                        if G.creator.mid in memid:
                            users.append(G.creator.mid)
                            user=G.creator.displayName
                        else:
                            users.append(memid[0])
                            user=memid[0].displayName
                        G_members.append(memid)
                        black=[]
                        B_list.append(black)
                        B_listName.append(black)
                        memid.clear()
                        nk_01.sendMessage(op.param1,"招待してくれてありがとう\nこのグループのnekosukeの使用権限者は、\n"+user+"さんです。\n使い方を確認したい場合は「help」と言ってください。")

                    if op.type==17:
                        G=nk_01.getGroup(op.param1)
                        gid=G.id
                        n=G_list.index(gid)#グループ番号
                        if op.param2 in B_list[n]:
                            try:
                                nks[1].kickoutFromGroup(op.param1,[op.param2])
                                nks[1].sendMessage(op.param1,"blacklistuserを退会させました")
                            except:
                                continue
                        elif op.param2 in G_members[n]:
                            ct=nk_01.getContact(op.param2)
                            G=nk_01.getGroup(op.param1)
                            nk_01.sendMessage(op.param1,ct.displayName+"さん\nようこそ"+G.name+"へ")

                        else:
                            if op.param2 in nkids:
                                n=nkids.index(op.param2)
                                if n==1:
                                    nks.append(nk_02)
                                elif n==2:
                                    nks.append(nk_03)
                                elif n==3:
                                    nks.append(nk_04)
                                elif n==4:
                                    nks.append(nk_05)
                                elif n==5:
                                    nks.append(nk_06)
                                elif n==6:
                                    nks.append(nk_07)
                                elif n==7:
                                    nks.append(nk_08)

                            else:
                                nk_01.sendMessage(op.param1,"メンバー登録をしてください")
                                nks[1].kickoutFromGroup(op.param1,[op.param2])

                    if op.type==19:
                        G=nk_01.getGroup(op.param1)
                        gid=G.id
                        n=G_list.index(gid)#グループ番号
                        if op.param2 in B_list[n]:
                            pass
                        else:
                            B_list[n].append(op.param2)
                        if op.param3 in G_members[n]:
                            G_members[n].remove(op.param2)
                            cn=nk_01.getContact(op.param2)
                            B_list[n].append(op.param2)
                            B_listName[n].append(cn.displayName)
                            name=cn.displayName
                            nk_01.kickoutFromGroup(to,[op.param2])
                            nk_01.sendMessage(to,name+"さんをブラックリストユーザーに追加しました")

                        elif op.param3 in nkids:
                            kicker=op.param2
                            n = nkids.index(op.param3)
                            lv_list.append(nks[n])
                            nks.pop(n)
                            nkids.remove(op.param3)
                            G=nks[1].getGroup(op.param1)
                            G.preventedJoinByTicket==False
                            nks[1].updateGroup(G)
                            T=nks[1].reissueGroupTicket(op.param1)
                            lv_list[0].acceptGroupInvitationByTicket(op.param1,T)
                            lv_list[0].kickoutFromGroup(op.param1,[kicker])
                            lv_list.pop(0)

                    if op.type==25:
                        msg=op.message
                        to=msg.to #groupid
                        _id=msg.id
                        cmd=msg.text
                        if msg.contentType==0:
                             if cmd in ["test"]:
                                 nk_01.sendMessage(to,"Hello")
                             elif cmd in ["help"]:
                                 allcmd='''===コマンド一覧===
 ┏━━━━━━━━━━━━━━━━━━
 ┣'creator'━作者名表示
 ┣'nk:join-(2~8 or all)'━nekosuke参加
 ┣'nk:leave-(2~8 or all)'━nekosuke退会
 ┣leave:masternekosuke━nekosuke001退会
 ┣nk:makeURL━グループURL作成
 ┣nk:getGroup━グループの情報を取得
 ┣'nk:addmember'━メンバー追加
 ┣'nkadduser'━権限者追加
 ┣nk:allmember━グループのメンバー全員の名前とID表示
 ┗━━━━━━━━━━━━━━━━━━━

 ===============================
 ☆☆☆☆☆☆☆create by hiroaki☆☆☆☆☆☆☆
 ===============================
 '''

                                 nk_01.sendMessage(to,allcmd)

                             elif cmd in ["nk:allin"]:
                                 G=nk_01.getGroup(to)
                                 G.preventedJoinByTicket=False
                                 nk_01.updateGroup(G)
                                 T=nk_01.reissueGroupTicket(to)
                                 nk_02.acceptGroupInvitationByTicket(to,T)
                                 nk_03.acceptGroupInvitationByTicket(to,T)
                                 nk_04.acceptGroupInvitationByTicket(to,T)
                                 nk_05.acceptGroupInvitationByTicket(to,T)
                                 nk_06.acceptGroupInvitationByTicket(to,T)
                                 nk_07.acceptGroupInvitationByTicket(to,T)
                                 nk_08.acceptGroupInvitationByTicket(to,T)

                             elif cmd in ["nk:allout"]:
                                 try:
                                     nk_03.leaveGroup(to)
                                     nk_04.leaveGroup(to)
                                     nk_05.leaveGroup(to)
                                     nk_06.leaveGroup(to)
                                     nk_07.leaveGroup(to)
                                     nk_08.leaveGroup(to)
                                 except:
                                     continue

                             elif cmd in ["leave:masternekosuke"]:
                                 G=nk_01.getGroup(to)
                                 gid=G.id
                                 n=G_list.index(gid)#グループ番号
                                 G_list.pop(n)
                                 G_listName.pop(n)
                                 G_members.pop(n)
                                 nk_01.sendMessage(to,"このグループの保護を解除します。\nご利用ありがとうございました。")
                                 nk_01.leaveGroup(to)
                             elif cmd in ["nk:makeURL"]:
                                 G=nk_01.getGroup(to)
                                 G.preventedJoinByTicket==False
                                 nk_01.updateGroup(G)
                                 T=nk_01.reissueGroupTicket(to)
                                 nk_01.sendMessage(to,"https://line.me/ti/g/"+str(T))

                             elif cmd in ["nk:allmember"]:

                                 G=nk_02.getGroup(to)
                                 memid=[i.mid for i in G.members]
                                 names=[i.displayName for i in G.members]
                                 m=len(memid)
                                 Roster = "メンバー一覧\n"#名簿
                                 for j in range(m):
                                     Roster = Roster + names[j] + "\n" + "\t" + "\t"+ "\t"+ "\t"+ "\t"+ "ID : " + str(memid[j]) + "\n"

                                 nk_02.sendMessage(to,Roster)
                                #for j in range(m):
                                    #nk_02.sendMessage(to,name[j]+"\nID : "+str(memid[j]))
                             elif cmd in ["nk:allgroup"]:
                                 for i in range(len(G_list)):
                                     nk_02.sendMessage(to,G_listName[i])

                             elif cmd in ["nk:sp"]:

                                 st=[]
                                 en=[]
                                 m=len(nks)
                                 for i in range(m):
                                     nks[i].sendMessage(to,".")
                                     st.append(time.time())
                                 for j in range(m):
                                     en.append(time.time())
                                     nks[j].sendMessage(to,"速度は\n%ssec"%(en[j]-st[j]))

                             elif cmd in ["blacklist"]:
                                  G=nk_01.getGroup(op.param1)
                                  gid=G.id
                                  n=G_list.index(gid)#グループ番号
                                  txt=""
                                  m=len(B_list[n])
                                  for i in range(m):
                                      txt=txt+"\n┣"+B_listName[n][i]

                                  nk_01.sendMessage(to,"ブラックリスト\n┏━━━━━━━━━━━━━━━━━━\n"+txt+"\n┗━━━━━━━━━━━━━━━━━━━")

                             elif "nk:join-" in cmd:
                                  n=int(cmd.strip('nk:join-'))
                                  G=nk_01.getGroup(to)
                                  G.preventedJoinByTicket=False
                                  nk_01.updateGroup(G)
                                  T=nk_01.reissueGroupTicket(to)
                                  allnks[n-1].acceptGroupInvitationByTicket(to,T)
                             elif "nk:leave-" in cmd:
                                 n=int(cmd.strip('nk:leave-'))
                                 allnks[n-1].leaveGroup(to)



                             elif cmd in ["addmember"]:
                                flag=1
                                nk_01.sendMessage(to,"追加する人の連絡先を貼ってください")
                             elif cmd in ["invite"]:
                                nk_01.inviteIntoGroup(to,['u2b9cfdb21068feeb5be01b9b41e29243'])

                    if op.type==26:
                        msg=op.message
                        to=msg.to #groupid
                        fr=msg._from#Sender
                        _id=msg.id
                        cmd=msg.text
                        G=nk_01.getGroup(to)
                        gid=G.id
                        n=G_list.index(gid)#Group number
                        if str(fr) == str(users[n]):
                            if msg.contentType==0:
                                if cmd in ["help"]:
                                    helpcommands="""===ALL_COMMANDS===
┏━━━━━━━━━━━━━━━━━━
┣'nk:profile'━nekosukeの情報表示
┣'nk:join-(2~8 or all)'━nekosuke参加
┣'nk:leave-(2~8 or all)'━nekosuke退会
┣'nk:leave_masternekosuke'━nekosuke001退会
┣'nk:makeURL'━グループURL作成
┣'nk:getGroup'━グループの情報を取得
┣'nk:diffusion_help'━拡散文の使い方
┣'nk:reception_setting'━拡散文の受信on/off切り替え
┣'nk:change_groupmaster'━nekosukeの権限者変更
┣'nk:addmember'━グループメンバー追加
┣'nk:BagRepoter'-バグの報告
┗━━━━━━━━━━━━━━━━━━━

===============================

☆☆☆☆☆☆☆☆☆ nekosukeBot ☆☆☆☆☆☆☆☆☆

===============================

-----------Ver.1.0.0-----------
"""
                                    nk_01.sendMessage(to,helpcommands)

                                elif cmd in ["testcmd"]:
                                    nk_01.sendMessage(to,"Hello World!")

                                elif cmd in ["nk:profile"]:
                                    nk.sendMessage(to,"Name:nekosuke001\nVersion:1.0.0\nURL:https://line.me/ti/p/8emibEwFMM")

                                elif cmd in ["nk:getGroup"]:
                                    gn=G.name
                                    mt=G.creator.displayName
                                    allmem=[i for i.displayName in G.members]
                                    l=len(allmem)
                                    temp=""
                                    for k in range(l):
                                        temp=temp+allmem[k]+"\n"
                                    nk_01.sendMessage(to,"GroupName : "+gn+"\nGroupCreator"+mt+"\n"+temp)
                                elif cmd in ["nk:leave_masternekosuke"]:
                                    G_list.pop(n)
                                    G_listName.pop(n)
                                    G_members.pop(n)
                                    nk_01.sendMessage(to,"このグループの保護を解除します。\nご利用ありがとうございました。")
                                    nk_01.leaveGroup(to)

                                elif  cmd in ["nk:makeURL"]:
                                     nk_01.sendMessage(to,"https://line.me/ti/g/"+str(G_URL[n]))

                                elif 'nk:join-' in cmd:
                                    obj=cmd.strip("nk:join-")
                                    if obj=="all":
                                         G.preventedJoinByTicket=False
                                         nk_02.acceptGroupInvitationByTicket(to,G_URL[n])
                                         nk_03.acceptGroupInvitationByTicket(to,G_URL[n])
                                         nk_04.acceptGroupInvitationByTicket(to,G_URL[n])
                                         nk_05.acceptGroupInvitationByTicket(to,G_URL[n])
                                         nk_06.acceptGroupInvitationByTicket(to,G_URL[n])
                                         nk_07.acceptGroupInvitationByTicket(to,G_URL[n])
                                         nk_08.acceptGroupInvitationByTicket(to,G_URL[n])
                                    else:
                                        try:
                                            cn=int(obj)
                                            G.preventedJoinByTicket=False
                                            allnks[cn-1].acceptGroupInvitationByTicket(to,G_URL[n])
                                        except:
                                            pass

                                elif 'nk:leave-' in cmd:
                                    obj=cmd.strip('nk:leave-')
                                    if obj=="all":
                                        try:
                                            nk_03.leaveGroup(to)
                                            nk_04.leaveGroup(to)
                                            nk_05.leaveGroup(to)
                                            nk_06.leaveGroup(to)
                                            nk_07.leaveGroup(to)
                                            nk_08.leaveGroup(to)
                                        except:
                                            continue
                                    else:
                                        try:
                                            cn=int(obj)
                                            allnks[cn-1].leaveGroup(to)
                                        except:
                                            pass

                                elif cmd in ["nk:reception_setting"]:
                                    G=nk_01.getGroup(to)
                                    gid=G.id
                                    n=G_list.index(gid)#グループ番号
                                    if Reception[n]==0:
                                        Reception[n]=1
                                        nk_01.sendMessage(to,"拡散文の受信をONにしました。")
                                    else:
                                        Reception[n]=0
                                        nk_01.sendMessage(to,"拡散文の受信をOFFにしました。")
                                elif cmd  in ["nk:change_groupmaster"]:
                                    flag[n]=2
                                    nk_01.sendMessage(to,"新しい権限者の連絡先をグループに送信してください。")

                                elif cmd in ["nk:addmember"]:
                                    flag[n]=1
                                    nk_01.sendMessage(to,"追加する人の連絡先を貼ってください")
                            elif msg.contentType==13:
                                if flag[n]==1:#add member
                                        invite = msg.contentMetadata["mid"]
                                        G_members[n].append(invite)
                                        ct=nk_01.getContact(invite)
                                        nk_01.sendMessage(to,ct.displayName+"さんをメンバーリストに追加しました\n"+ct.displayName+"さんをこのグループに招待してあげてください。")
                                        flag[n]=0
                                elif flag[n]==2:#change_groupmaster
                                    usable_person=msg.contentMetadata["mid"]
                                    if usable_person in G_members[n]:
                                        users[n]=usable_person
                                        nk_01.sendMessage(to,"権限者を"+msg.contentMetadata["displayName"]+"さんに変更しました。")
                                        flag[n]=0
                                    else:
                                        nk_01.sendMessage(to,msg.contentMetadata["displayName"]+"さんをメンバーに追加してください。\nメンバーの追加は'nk:addmember'からできます。")
                                        flag[n]=0

                        else:
                            if cmd in ["nk:BagRepoter"]:
                                nk_01.sendMessage(to,"不具合がございましたら下記のメールアドレスにバグの内容を報告お願いいたします。\n===================\nmail:samplenekosuke001@gmail.com")
                                template="""==テンプレート==
- - - - - - - - - - - - - - -
To samplenekosuke001@gmail.com
件名 nekosuke_BagRepoter

~ここにバグの内容を書いてください~
"""
                                nk_01.sendMessage(to,template)
                except:
                    print("ERROR!!")
                    import traceback
                    traceback.print_exc()
                    pass

                finally:
                    nk_01.revision=max(op.revision,nk_01.revision)
