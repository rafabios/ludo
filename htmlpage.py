from db import queryDBall


def htmlGen():
    list = []
    allHtml = ''
    # generate html tags
    for bg in queryDBall():
        #print(bg)
        #test = '<td><span class="badge badge-primary">Leilao</span></td><td>Lacrado</td><td class="sorting_1"><b>{}</b></td><td>{}</td><td><a href="https://ludopedia.com.br/anuncio?id_anuncio=222399" target="new">Link</a></td><td>{}</td></tr>'.format(bg[1],bg[0],bg[2])
        htmlTd =  '<td><span class="badge badge-primary">Leilao</span><td class="sorting_1"><b>{}</b></td><td>{}</td><td>{}</td></tr>'.format(bg[1],bg[0],bg[2][0:19])
        #print(test)
        list.append(htmlTd)
        allHtml = allHtml + "\n" + htmlTd


    # generate template html
    with open('static/ludo-template.html', 'r', encoding='utf-8') as file:
        data = file.readlines()
    
    #print(data)
    data[150] = allHtml
    
    with open('static/index.html', 'w', encoding='utf-8') as file:
        file.writelines(data)    
        file.close()    

