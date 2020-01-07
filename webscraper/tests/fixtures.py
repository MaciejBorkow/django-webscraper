class ExamplePage:
    """ snippet of https://pl.wikipedia.org/wiki/Volkswagen_Golf - date: 13.12.2019"""
    url = r"https://pl.wikipedia.org/wiki/Volkswagen_Golf "
    raw_text = """
    <body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject mw-editable page-Volkswagen_Golf rootpage-Volkswagen_Golf skin-vector action-view">
    <div class="thumb tleft"><div class="thumbinner" style="width:222px;"><a href="/wiki/Plik:Vw_golf_1_h_sst.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Vw_golf_1_h_sst.jpg/220px-Vw_golf_1_h_sst.jpg" decoding="async" width="220" height="165" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Vw_golf_1_h_sst.jpg/330px-Vw_golf_1_h_sst.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Vw_golf_1_h_sst.jpg/440px-Vw_golf_1_h_sst.jpg 2x" data-file-width="1024" data-file-height="768" /></a> </div></div>
    <div class="thumb tleft"><div class="thumbinner" style="width:222px;"><a href="/wiki/Plik:VW_Golf_I_front_20080930.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/VW_Golf_I_front_20080930.jpg/220px-VW_Golf_I_front_20080930.jpg" decoding="async" width="220" height="136" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/VW_Golf_I_front_20080930.jpg/330px-VW_Golf_I_front_20080930.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4a/VW_Golf_I_front_20080930.jpg/440px-VW_Golf_I_front_20080930.jpg 2x" data-file-width="1698" data-file-height="1053" /></a></div></div>
    <div class="thumb tleft"><div class="thumbinner" style="width:222px;"><a href="/wiki/Plik:VW_Golf_I_rear_20080930.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a5/VW_Golf_I_rear_20080930.jpg/220px-VW_Golf_I_rear_20080930.jpg" decoding="async" width="220" height="143" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a5/VW_Golf_I_rear_20080930.jpg/330px-VW_Golf_I_rear_20080930.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a5/VW_Golf_I_rear_20080930.jpg/440px-VW_Golf_I_rear_20080930.jpg 2x" data-file-width="1650" data-file-height="1074" /></a>  </div></div>
    <div class="thumb tleft"><div class="thumbinner" style="width:222px;"><a href="/wiki/Plik:VW_Golf_I_rear_20080208.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/6/66/VW_Golf_I_rear_20080208.jpg/220px-VW_Golf_I_rear_20080208.jpg" decoding="async" width="220" height="130" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/6/66/VW_Golf_I_rear_20080208.jpg/330px-VW_Golf_I_rear_20080208.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/6/66/VW_Golf_I_rear_20080208.jpg/440px-VW_Golf_I_rear_20080208.jpg 2x" data-file-width="1716" data-file-height="1017" /></a>  </div></div>
    <div class="thumb tleft"><div class="thumbinner" style="width:222px;"><a href="/wiki/Plik:P089_VW_Golf_1_GTi_2.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/ab/P089_VW_Golf_1_GTi_2.jpg/220px-P089_VW_Golf_1_GTi_2.jpg" decoding="async" width="220" height="165" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/ab/P089_VW_Golf_1_GTi_2.jpg/330px-P089_VW_Golf_1_GTi_2.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/ab/P089_VW_Golf_1_GTi_2.jpg/440px-P089_VW_Golf_1_GTi_2.jpg 2x" data-file-width="2048" data-file-height="1536" /></a>  <div class="thumbcaption"></div></div></div>
    <p><b>Volkswagen Golf I</b> został zaprezentowany po raz pierwszy w 1974 roku.
    </p><p>Geneza powstania modelu Golf sięga końca lat 60., kiedy to zarząd <a href="/wiki/Volkswagen_AG" title="Volkswagen AG">Volkswagen AG</a> podjął decyzję o budowie małego samochodu kompaktowego posiadającego <a href="/wiki/Nap%C4%99d_przedni" title="Napęd przedni">przedni napęd</a> 
    </p>
    <tr>
    </tr>
    </body>
    """
    img_src_raw = {"//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Vw_golf_1_h_sst.jpg/220px-Vw_golf_1_h_sst.jpg",
               "//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/VW_Golf_I_front_20080930.jpg/220px-VW_Golf_I_front_20080930.jpg",
               "//upload.wikimedia.org/wikipedia/commons/thumb/a/a5/VW_Golf_I_rear_20080930.jpg/220px-VW_Golf_I_rear_20080930.jpg",
               "//upload.wikimedia.org/wikipedia/commons/thumb/6/66/VW_Golf_I_rear_20080208.jpg/220px-VW_Golf_I_rear_20080208.jpg",
               "//upload.wikimedia.org/wikipedia/commons/thumb/a/ab/P089_VW_Golf_1_GTi_2.jpg/220px-P089_VW_Golf_1_GTi_2.jpg"
               }
    text = """

 

 
 
 
Volkswagen Golf I został zaprezentowany po raz pierwszy w 1974 roku.
    Geneza powstania modelu Golf sięga końca lat 60., kiedy to zarząd Volkswagen AG podjął decyzję o budowie małego samochodu kompaktowego posiadającego przedni napęd




"""
    img_src_normalized = {'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/VW_Golf_I_front_20080930.jpg/220px-VW_Golf_I_front_20080930.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/VW_Golf_I_rear_20080930.jpg/220px-VW_Golf_I_rear_20080930.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/VW_Golf_I_rear_20080208.jpg/220px-VW_Golf_I_rear_20080208.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Vw_golf_1_h_sst.jpg/220px-Vw_golf_1_h_sst.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/P089_VW_Golf_1_GTi_2.jpg/220px-P089_VW_Golf_1_GTi_2.jpg'}

text_loremipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."