import random,pygame,sys,time

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    WIDTH,HEIGHT=550,700
    WI,HE=550,550
    WHITE=(255,255,255)
    win=pygame.display.set_mode((WIDTH,HEIGHT))
    bgi=pygame.image.load('bgi.jpg')
    bgi=pygame.transform.scale(bgi,(WIDTH,HEIGHT))
    fbgi=pygame.image.load('fbgi.jpg')
    fbgi=pygame.transform.scale(fbgi,(WIDTH,HEIGHT))
    di=pygame.image.load('di.png')
    icon=pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    f1=pygame.font.Font('CandyBeans.otf',30)
    f2=pygame.font.Font(None,80)
    t1=f1.render('Presiona "q" para salir',True,WHITE)
    t1_rect=t1.get_rect(center=(WIDTH//2,HEIGHT-110))
    t2=f1.render('Presiona "r" para reiniciar',True,WHITE)
    t2_rect=t2.get_rect(center=(WIDTH//2,HEIGHT-40))
    ss=pygame.mixer.Sound('ss.wav')
    gs=pygame.mixer.Sound('gs.wav')
    bs=pygame.mixer.Sound('bs.wav')
    fs=pygame.mixer.Sound('fs.mp3')
    nums=list(range(1,9))*2
    random.shuffle(nums)
    board=[[''for _ in range(4)]for _ in range(4)]
    board2=[[''for _ in range(4)]for _ in range(4)]
    game_over=False
    sel=[]
    selrow=[]
    selcol=[]
    for i in range(4):
        for j in range(4):
            numero=nums.pop()
            board[i][j]=numero
            board2[i][j]=numero
    def draw_board():
        for row in range(4):
            for col in range(4):
                draw_default(row,col)
                if board[row][col]==9:
                    draw_num(row,col)
                if all(board[row][col]==9 for row in range(4) for col in range(4)):
                    draw_f(col,row)
    def draw_num(col,row):
        cell_center_x=col*WIDTH//4+(WIDTH//4)//2
        cell_center_y=row*HE//4+(HE//4)//2
        current_num=f2.render(str(board2[row][col]),True,WHITE)
        current_num_rect=current_num.get_rect(center=(cell_center_x,cell_center_y))
        win.blit(current_num,current_num_rect)
    def draw_f(col,row):
        win.blit(fbgi,(0,0))
        win.blit(t2,t2_rect)
    def draw_default(col,row):
        cell_center_x=col*WIDTH//4+(WIDTH//4)//2
        cell_center_y=row*HE//4+(HE//4)//2
        di_rect=di.get_rect(center=(cell_center_x,cell_center_y))
        win.blit(di,di_rect)
    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    game_over=True
                elif event.key==pygame.K_r:
                    main()
            win.blit(bgi,(0,0))
            try:
                if event.type==pygame.MOUSEBUTTONDOWN:
                    x,y=event.pos
                    row=x//(HE//4)
                    col=y//(WI//4)
                    sel.append(board2[col][row])
                    selrow.append(row)
                    selcol.append(col)
                    draw_num(row,col)
                    ss.play()
                    if len(sel)==2:
                        if sel[0]==sel[1]:
                            if selrow[0]!=selrow[1] or selcol[0]!=selcol[1]:
                                board[selrow[0]][selcol[0]]=9
                                board[selrow[1]][selcol[1]]=9
                                gs.play()
                                selrow=[]
                                selcol=[]
                                sel=[]
                        else:
                            bs.play()
                            selrow=[]
                            selcol=[]
                            sel=[]
                        selrow=[]
                        selcol=[]
                        sel=[]
                    if all(board[row][col]==9 for row in range(4) for col in range(4)):
                        fs.play()
            except:pass
            win.blit(t1,t1_rect)
            win.blit(t2,t2_rect)
            draw_board()
            pygame.display.update()
    pygame.quit()
    sys.exit()
main()