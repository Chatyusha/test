from mafuLib.linepy import *
import time
import timeit


nk=LINE()
print('nk=LINE("' + str(nk.authToken)+')"')

m_id=nk.getProfile().mid

while True:
    try:
        ops=nk.poll.fetchOperations(nk.revision,50)
    except:
        continue

    if ops!=None:
        for op in ops:
            try:
                if op.type==13:
                    if op.param3==m_id:
                        nk.acceptGroupInvitation(op.param1)

                if op.type==26:
                    msg=op.message
                    if msg.contentType==0:
                        to=msg.to
                        fr=msg._from
                        _id=msg.id
                        cmd=msg.text

                        if cmd in ["group"]:
                            try:
                                G=nk.getGroup(to)
                                ids=[h.mid for h in G.members]
                                cra=""
                                if G.creator.mid in ids:
                                    cra=G.creator.displayName
                                else:
                                    cra="不在"
                                member=[i.displayName for i in G.members]
                                n=len(member)
                                mem=""
                                for j in range(n):
                                    mem=mem+member[j]+"さん\n"
                                G.preventedJoinByTicket=False
                                T=nk.reissueGroupTicket(to)
                                print("n")
                                nk.sendMessage(to,"Group_Creator:"+cra+"さん\n\n"+"All_Members:\n"+mem+"\n\nGroup_URL:\nhttps://line.me/ti/g/"+str(T))



                            except:
                                print("Error")
                                pass

                        elif cmd in ["test"]:
                            nk.sendMessage(to,"hello\tWorld")

            except:
                print("ERROR!!")
                import traceback
                traceback.print_exc()
                pass

            finally:
                nk.revision=max(op.revision,nk.revision)
