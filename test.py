import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
#x = np.array([-0.02472375806114572, 0.5109354333784081, 0.5441520215409804, -0.6180769235329646, -0.21448967241022238, 0.03955942018301116])

#a6bddb
#7fcdbb
#3352FF"
#1c9099
#33E6FF

word2vec_gmm = np.array([-0.095056, -0.127448, -0.123424, -0.132376, -0.095482, -0.105638, -0.255478])
word2vec_kmeans = np.array([-0.123848,-0.1245,-0.103624, -0.078768, -0.073148, -0.11385, -0.216802])
word2vec_kmedoids = np.array([-0.21825, -0.22564, -0.21434, -0.22781, -0.18083, -0.18421, -0.19015])
word2vec_agglo = np.array([-0.05214, -0.04468, -0.02199, -0.0371, 0.03819, -0.07126, -0.29372])
X = [300, 250, 200, 150, 100, 50, 10]
plt.plot(X, word2vec_gmm, marker = "o", label='GMM')
plt.plot(X, word2vec_kmeans, marker = "o", label='KMeans')
plt.plot(X, word2vec_kmedoids, marker = "o", label='KMedoids')
plt.plot(X, word2vec_agglo, marker = "o", label='Agglomertive')
plt.legend()
plt.xlabel("Dimensions")
plt.ylabel("NPMI score")
plt.title("Word2Vec")
plt.show(block=True)


ft_gmm = np.array([-0.179342,-0.16654399999999997,-0.132826, -0.09831999999999999,-0.07516199999999999, -0.05738,-0.245326])
ft_kmeans = np.array([-0.21415199999999998,-0.16694,-0.142072,-0.115066,-0.10752599999999998,-0.108698,-0.23159800000000003])
ft_kmedoids = np.array([-0.25637,-0.28282,-0.21352,-0.15311,-0.16061,-0.0843,-0.21936])
ft_agglo = np.array([-0.15514,-0.16494,-0.10552,-0.08263,-0.07523,-0.05542,-0.27672])
X = [300, 250, 200, 150, 100, 50, 10]
plt.plot(X, ft_gmm,marker = "o", label='GMM')
plt.plot(X, ft_kmeans, marker = "o", label='KMeans')
plt.plot(X, ft_kmedoids, marker = "o", label='KMedoids')
plt.plot(X, ft_agglo, marker = "o", label='Agglomertive')
plt.xlabel("Dimensions")
plt.ylabel("NPMI score")
plt.title("Fasttext")
plt.legend()
plt.show(block=True)






sp_gmm = np.array([-0.189588, -0.143026,-0.118854,-0.135458,-0.104766,-0.150414,-0.247276])
sp_kmeans = np.array([-0.034006,-0.018094,-0.031844,-0.069102,-0.074584,-0.122374,-0.252426])
sp_kmedoids = np.array([-0.05276,0.0168,0.01608, -0.03257, -0.09852,-0.11127,-0.29612])
sp_agglo = np.array([-0.0194,-0.01696,-0.07962,-0.07661,-0.04033,-0.16071,-0.31043])
X = [300, 250, 200, 150, 100, 50, 10]
plt.plot(X, sp_gmm,marker = "o", label='GMM')
plt.plot(X, sp_kmeans, marker = "o", label='KMeans')
plt.plot(X, sp_kmedoids, marker = "o", label='KMedoids')
plt.plot(X, sp_agglo, marker = "o", label='Agglomertive')
plt.xlabel("Dimensions")
plt.ylabel("NPMI score")
plt.title("Spherical")
plt.legend()
plt.show(block=True)

g_kmeans = np.array([-0.249584,-0.264816,-0.294254,-0.31147,-0.342222,-0.324684,-0.371928])
g_kmedoids = np.array([-0.30439,-0.31076,-0.34063,-0.31675,-0.37252,-0.3429,-0.41878])
g_agglo = np.array([-0.22928,-0.30184,-0.26225,-0.2474,-0.248,-0.23151,-0.37022])
g_gmm = np.array([-0.198256, -0.1967,-0.209454,-0.211876,-0.258184,-0.285262,-0.34213])
X = [300, 250, 200, 150, 100, 50, 10]
plt.plot(X, g_gmm,marker = "o", label='GMM')
plt.plot(X, g_kmeans, marker = "o", label='KMeans')
plt.plot(X, g_kmedoids, marker = "o", label='KMedoids')
plt.plot(X, g_agglo, marker = "o", label='Agglomertive')
plt.xlabel("Dimensions")
plt.ylabel("NPMI score")
plt.title("Glove")
plt.legend()
plt.show(block=True)


dim = np.array([768, 500, 400, 300, 250, 200, 150, 100, 50, 10])
lyr12 = np.array([0.161697, 0.15656, 0.11519,0.034606, 0.006728, -0.021342, -0.05588800000000001, -0.06703200000000001, -0.17069600000000001, -0.32401])
lyr11 = np.array([0.11403,0.062154,0.017604,-0.015588000000000001,-0.06933199999999999,-0.132994,-0.111646,-0.17278,-0.282708,-0.403918])
lyr10 = np.array([0.09253399999999999,0.035986000000000004,0.030203999999999998,0.017714,0.005592,-0.05425,-0.08741800000000001,-0.08855199999999999,-0.185608, -0.381176])
lyr9 = np.array([0.04964799999999999,0.0068800000000000016,-0.006922,-0.026282,-0.090058,-0.08491,-0.17250000000000001,-0.158372,-0.22822599999999998,-0.389024])
lyr8 = np.array([0.023212,5.8000000000000935e-05,-0.030938,-0.085754,-0.151664,-0.11097399999999999,-0.198902,-0.178288,-0.25411799999999996,-0.444798])
lyr7 = np.array([-0.008797999999999997,-0.06860000000000001,-0.066878,-0.08268,-0.139632,-0.203412,-0.25107799999999997,-0.22641400000000003,-0.27910999999999997,-0.480824])
lyr6 = np.array([-0.05299,-0.12040799999999999,-0.08477399999999999,-0.19646800000000003,-0.246,-0.247992,-0.30827400000000005,-0.27846399999999993,-0.30454400000000004,-0.432822])
lyr5 = np.array([-0.067344,-0.13154,-0.140738,-0.21198199999999998,-0.22132999999999997,-0.271752,-0.34271,-0.302914,-0.32835000000000003,-0.49747])
lyr4 = np.array([-0.170618,-0.195924,-0.20729800000000004,-0.27004,-0.311886,-0.336782,-0.379356,-0.365442,-0.38995199999999997,-0.47887399999999997])
lyr3 = np.array([-0.159306,-0.214862, -0.235274,-0.248,-0.324192,-0.32764000000000004,-0.37998800000000005,-0.38968600000000003,-0.354896,-0.496868])
lyr2 = np.array([-0.21956199999999998,-0.241516,-0.248188,-0.291942,-0.303908,-0.335834, -0.352614, -0.33505799999999997, -0.39720199999999994,-0.388082])
lyr1 = np.array([-0.230438, -0.247326, -0.279686,-0.314062,-0.30792, -0.37167, -0.374856, -0.39151, -0.420286, -0.383046])
plt.plot(dim, lyr1, marker = "o", label='layer 1')
#plt.plot(dim, lyr2, marker = "o", label='layer 2')
plt.plot(dim, lyr3, marker = "o", label='layer 3')
#plt.plot(dim, lyr4, marker = "o", label='layer 4')
#plt.plot(dim, lyr5, marker = "o", label='layer 5')
plt.plot(dim, lyr6, marker = "o", label='layer 6')
#plt.plot(dim, lyr7, marker = "o", label='layer 7')
#plt.plot(dim, lyr8, marker = "o", label='layer 8')
plt.plot(dim, lyr9, marker = "o", label='layer 9')
#plt.plot(dim, lyr10, marker = "o", label='layer 10')
#plt.plot(dim, lyr11, marker = "o", label='layer 11')
plt.plot(dim, lyr12, marker = "o", label='layer 12')
plt.xlabel("Dimension")
plt.ylabel("NPMI score")
plt.title("GMM")
plt.legend()
plt.show(block=True)

lyr12 = np.array([-0.08164,-0.09777,-0.13825,-0.12572,-0.12459,-0.12294000000000001,-0.0847,-0.19067,-0.1556,-0.31846])
lyr11 = np.array([-0.20078,-0.17177,-0.19232,-0.23671999999999999,-0.21476,-0.2046,-0.27191,-0.2143,-0.25674,-0.40254])
lyr10 = np.array([-0.12389999999999998,-0.12569,-0.10267,-0.17082,-0.13458,-0.15885,-0.17721,-0.23606,-0.27321,-0.4563499999999999])
lyr9 = np.array([-0.15404,-0.17871,-0.21696,-0.20799000000000004,-0.29631,-0.24236,-0.25184,-0.25864,-0.32088,-0.43605])
lyr8 = np.array([-0.16969,-0.19665,-0.27888,-0.23969000000000001,-0.22074,-0.24591,-0.24085,-0.26726,-0.32734,-0.379])
lyr7 = np.array([-0.24657999999999997,-0.26574,-0.29806,-0.25394,-0.38254,-0.32616,-0.3408,-0.28871,-0.33247,-0.40943000000000007])
lyr6 = np.array([-0.38068,-0.34792,-0.33571,-0.38978,-0.33514,-0.36788,-0.28868,-0.21217999999999998,-0.38605,-0.4438])
lyr5 = np.array([-0.35386,-0.38823,-0.35831,-0.36621,-0.36724,-0.30451,-0.3289,-0.35887,-0.36654,-0.4381])
lyr4 = np.array([-0.36866,-0.35375,-0.39143,-0.26714,-0.37901,-0.35254,-0.28646,-0.40478,-0.34803,-0.45955])
lyr3 = np.array([-0.43113999999999997,-0.36713,-0.38517,-0.35114,-0.36123,-0.36175,-0.34608,-0.2906,-0.37289,-0.44192])
lyr2 = np.array([-0.44237000000000004,-0.37385,-0.4204899999999999,-0.44027000000000005,-0.30716,-0.3402,-0.35396,-0.29408,-0.37281,-0.42286999999999997])
lyr1 = np.array([-0.34369,-0.35162,-0.36884,-0.32911,-0.36786,-0.31709,-0.38224,-0.39106,-0.35495,-0.39302])
plt.plot(dim, lyr1, marker = "o", label='layer 1')
#plt.plot(dim, lyr2, marker = "o", label='layer 2')
plt.plot(dim, lyr3, marker = "o", label='layer 3')
#plt.plot(dim, lyr4, marker = "o", label='layer 4')
#plt.plot(dim, lyr5, marker = "o", label='layer 5')
plt.plot(dim, lyr6, marker = "o", label='layer 6')
#plt.plot(dim, lyr7, marker = "o", label='layer 7')
#plt.plot(dim, lyr8, marker = "o", label='layer 8')
plt.plot(dim, lyr9, marker = "o", label='layer 9')
#plt.plot(dim, lyr10, marker = "o", label='layer 10')
#plt.plot(dim, lyr11, marker = "o", label='layer 11')
plt.plot(dim, lyr12, marker = "o", label='layer 12')
plt.xlabel("Dimension")
plt.ylabel("NPMI score")
plt.title("Agglo")
plt.legend()
plt.show(block=True)


lyr12 = np.array([-0.13868399999999997,-0.15222,-0.174528,-0.17212,-0.17194000000000004,-0.146994,-0.148786,-0.156772,-0.21499799999999997,-0.29142000000000007])
lyr11 = np.array([-0.22721200000000003,-0.23497000000000004,-0.23126599999999997,-0.25553,-0.26586999999999994,-0.270162,-0.26455399999999996,-0.271032,-0.26071799999999995,-0.369692])
lyr10 = np.array([-0.219592,-0.2395,-0.247002,-0.24159199999999997,-0.23235200000000003,-0.23212799999999997,-0.24419,-0.239068,-0.264648,-0.36723000000000006])
lyr9 = np.array([-0.24716,-0.27383199999999996,-0.286216,-0.307174,-0.32424400000000003,-0.28974,-0.293498,-0.267934,-0.30566799999999994,-0.43151])
lyr8 = np.array([-0.329296,-0.296998,-0.334276,-0.341078,-0.346544,-0.35145800000000005,-0.33229200000000003,-0.323806,-0.31471000000000005,-0.406158])
lyr7 = np.array([-0.40228,-0.41664599999999996,-0.390794,-0.36814800000000003,-0.41125,-0.384952,-0.391832,-0.34848,-0.345066,-0.452266])
lyr6 = np.array([-0.408108,-0.41315799999999997,-0.426032,-0.42159599999999997,-0.411376,-0.413718,-0.42562999999999995,-0.394246,-0.39050799999999997,-0.420352])
lyr5 = np.array([-0.412028,-0.402716,-0.422466,-0.42806999999999995,-0.424022,-0.42123599999999994,-0.398862,-0.402538,-0.40023200000000003,-0.45043])
lyr4 = np.array([-0.4623799999999999,-0.4454560000000001,-0.404638,-0.397108,-0.4151000000000001,-0.386984,-0.370036,-0.363248,-0.377106,-0.44715799999999994])
lyr3 = np.array([-0.41002400000000006,-0.40545200000000003,-0.405244,-0.360666,-0.39156399999999997,-0.368744,-0.329984,-0.33968999999999994,-0.35229999999999995,-0.434682])
lyr2 = np.array([-0.41786200000000007,-0.396246,-0.384438,-0.393632,-0.38143,-0.34454599999999996,-0.343472,-0.348326,-0.341514,-0.37384399999999995])
lyr1 = np.array([-0.380526,-0.41127,-0.36919599999999997,-0.35638,-0.36342399999999997,-0.365006,-0.346496,-0.355144,-0.39367199999999997,-0.43193400000000004])


plt.plot(dim, lyr1, marker = "o", label='layer 1')
#plt.plot(dim, lyr2, marker = "o", label='layer 2')
plt.plot(dim, lyr3, marker = "o", label='layer 3')
#plt.plot(dim, lyr4, marker = "o", label='layer 4')
#plt.plot(dim, lyr5, marker = "o", label='layer 5')
plt.plot(dim, lyr6, marker = "o", label='layer 6')
#plt.plot(dim, lyr7, marker = "o", label='layer 7')
#plt.plot(dim, lyr8, marker = "o", label='layer 8')
plt.plot(dim, lyr9, marker = "o", label='layer 9')
#plt.plot(dim, lyr10, marker = "o", label='layer 10')
#plt.plot(dim, lyr11, marker = "o", label='layer 11')
plt.plot(dim, lyr12, marker = "o", label='layer 12')
plt.xlabel("Dimension")
plt.ylabel("NPMI score")
plt.title("KMeans")
plt.legend()
plt.show(block=True)

lyr12 = np.array([-0.27314,-0.31163,-0.32234,-0.30653,-0.34868,-0.33719,-0.30288,-0.38736,-0.34661,-0.33916])
lyr11 = np.array([-0.39641,-0.36355,-0.37347,-0.38764,-0.37756,-0.36938,-0.36659,-0.37328,-0.42321,-0.40435])
lyr10 = np.array([-0.32858,-0.29903,-0.29473,-0.32148,-0.34493,-0.39356,-0.39808,-0.39244,-0.35111,-0.4307])
lyr9 = np.array([-0.23508,-0.22949999999999998,-0.25669,-0.30173,-0.33216,-0.32656,-0.33934,-0.3596,-0.33214,-0.46405])
lyr8 = np.array([-0.30746,-0.37687,-0.35774,-0.37093,-0.40417,-0.38451,-0.37008,-0.35741,-0.35699,-0.40338])
lyr7 = np.array([-0.33392,-0.36134,-0.3931,-0.39142,-0.35643,-0.37834,-0.39048,-0.28721,-0.31558,-0.43088])
lyr6 = np.array([-0.37695,-0.32108,-0.32695,-0.3647,-0.4258,-0.43949,-0.39238,-0.36295,-0.34972,-0.49229])
lyr5 = np.array([-0.39418,-0.36849,-0.40306999999999993,-0.39651,-0.36001,-0.35353,-0.40554000000000007,-0.38096,-0.36523,-0.438430])
lyr4 = np.array([-0.32821,-0.35967,-0.35626,-0.33941,-0.33022,-0.35897,-0.33464,-0.36675,-0.36912,-0.36956])
lyr3 = np.array([-0.29987,-0.29735,-0.34067,-0.37957,-0.33302,-0.37251,-0.37559,-0.38346,-0.34869,-0.47112])
lyr2 = np.array([-0.30826,-0.34729,-0.34407,-0.32783,-0.37496,-0.35409,-0.35486,-0.32297,-0.37366,-0.40534])
lyr1 = np.array([-0.28755,-0.29899,-0.3469,-0.36305,-0.40121,-0.37232,-0.36184,-0.352,-0.43206,-0.36539])

plt.plot(dim, lyr1, marker = "o", label='layer 1')
#plt.plot(dim, lyr2, marker = "o", label='layer 2')
plt.plot(dim, lyr3, marker = "o", label='layer 3')
#plt.plot(dim, lyr4, marker = "o", label='layer 4')
#plt.plot(dim, lyr5, marker = "o", label='layer 5')
plt.plot(dim, lyr6, marker = "o", label='layer 6')
#plt.plot(dim, lyr7, marker = "o", label='layer 7')
#plt.plot(dim, lyr8, marker = "o", label='layer 8')
plt.plot(dim, lyr9, marker = "o", label='layer 9')
#plt.plot(dim, lyr10, marker = "o", label='layer 10')
#plt.plot(dim, lyr11, marker = "o", label='layer 11')
plt.plot(dim, lyr12, marker = "o", label='layer 12')
plt.xlabel("Dimension")
plt.ylabel("NPMI score")
plt.title("KMedoids")
plt.legend()
plt.show(block=True)


word2vec_agglo = np.array([ -0.2253, -0.2076, -0.1792, -0.1779, -0.1721, -0.1842])

fasttext_agglo = np.array([-0.1864, -0.1616, -0.1494, -0.1856, -0.1862, -0.2213])

spherical_agglo  = np.array([-0.3097, -0.3142, -0.2561, -0.2402, -0.1155, -0.1350])

bert_agglo = np.array([ -0.3675,-0.3142,-0.2849, -0.2746, -0.2667, -0.2485])
