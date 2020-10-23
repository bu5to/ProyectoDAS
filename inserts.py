# coding=utf-8

# 1 - imports
from datetime import date

from base import Session, engine, Base
from main import Marca, Usuario, Coche


# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# # 4 - create movies
u1 = Usuario("jebusto", "jebusto@gmail.com", "pass")
u2 = Usuario("elpepe", "elpepe@gmail.com", "josemanuel")

m1 = Marca("Ford", "EEUU") 
m2 = Marca("Mercedes Benz", "EEUU") 
m3 = Marca("BMW", "Alemania") 
m4 = Marca("Audi", "Alemania") 
m5 = Marca("Renault", "Francia") 
m6 = Marca("Volvo", "Suecia") 
m7 = Marca("Toyota", "Japón") 

c1 = Coche(m1, "Fiesta", 2004, 127500, "Gasolina", 80, "Ford Fiesta trend 1.4 gasolina del 2004 Con distintivo medio ambiental Pantalla táctil de 7 Rueda de recambio, dos llaves 127.500 km, se entrega con todas las revisiones hechas, ITV, etc...", 2300, "https://www.anunciosmarinaalta.com/uploads/2012/01/ford-fiesta-tren-2003-para-vender-34572-2.jpg")
c2 = Coche(m1, "Focus", 1999, 144200, "Gasolina", 100, "Ford focus sedan, bien cuidado, funciona perfectamente, poco kilometraje real, elevalunas eléctrico, cierre centralizado, aire acondicionado perfecto, llantas recién cambiadas, motor y caja perfecto,itv en vigor.", 1900, "https://cdn.wallapop.com/images/10420/96/h2/__/c10420p555069191/i1661844235.jpg")
c3 = Coche(m1, "Mondeo", 2001, 153404, "Gasolina", 125, "Único dueño. Mantenimiento al día. Vehículo amplio y espacioso, muy cuidado. Posibilidad de admitir vehículo como parte del pago. Garantía 12 meses (según condiciones). Se entregan vehículo en todo el territorio nacional (condiciones y costos a verificar) Coche en perfecto estado y totalmente revisado.", 1450, "https://img.milanuncios.com/fg/2943/29/294329457_1.jpg?VersionId=ugc6B6wwhoGwNroFnvoJUlIWaQzFcTmq")
c4 = Coche(m2, "Clase C", 2004, 260000, "Diesel", 143, "Cambio automático Abs Srs 4 Airbags Faros antiniebla Cierre centralizado Climatizador bizona Dirección asistida 4 Elevalunas eléctricos Control de velocidad Asientos eléctricos Asientos calefactables Sensor de luces Retrovisores eléctricos Llantas de aleación Ordenador de abordo Volante multifunción Muy buen estado", 3800, "https://www.grupocompostela.com/Archivos/Fotos/Coches_fotos/mercedes_benz-clase_c-2002-segunda_mano-santiago-compostela-coruna-090516_15-146278994263.jpg")
c5 = Coche(m2, "Clase E", 2002, 207563, "Gasolina", 224, "Considerada de las mejores generaciones de clase e de la historia, la w211 es también una de las que mejor ha mostrado la filosofía del modelo: confort, lujo y fiabilidad. esta unidad cuenta con histórico de mantenimiento a través de libro de revisiones y facturas. su motor de 6 cilindros y 224 cv es muy equilibrado y responde con suavidad o contundencia según las necesidades.", 4300, "https://img.milanuncios.com/fg/2677/63/267763745_1.jpg?VersionId=blgaOpvVhvKs6pLWMb5rhH3FJPWsmONu")
c6 = Coche(m2, "Clase E", 1988, 407000, "Diesel", 130, "Clásico, ITV pasada hasta junio 2021, funciona perfectamente, tiene algunas cositas para hacer por la edad", 2200, "https://3.bp.blogspot.com/-xWmDpjooJaA/U4I7-qELT_I/AAAAAAAAFes/dqIgQXP2O3A/s1600/DSCF1627.JPG")
c7 = Coche(m3, "Serie 3", 1987, 135000, "Gasolina", 150, "Bmw 325 e30 coupé automático, pack mtecnic exterior comprado en bmw . Libros de mantenimiento. Coche en perfecto Estado de mantenimiento. Misma familia. Primero con matrículas turistas.", 8450, "https://img.milanuncios.com/fg/3456/30/345630586_3.jpg?VersionId=8vaVJq9po2PBc4epwca1vSU3LWHgABSi")
c8 = Coche(m3, "Serie 7", 2012, 188696, "Diesel", 258, "llantas de aleación ligera de radios dobles (estilo 648 m), cambio automático deportivo, cámara para marcha atrás, bmw display key, dispositivo de alarma con mando a distancia, acceso confort, paquete deportivo m, climatizador con regulación de 4 zonas", 22800, "https://www.km77.com/images/medium/0/7/4/3/bms-serie-7-exterior-lateral.310743.jpg")
c9 = Coche(m4, "A4", 2005, 305000, "Diesel", 140, "Coche en buen estado, correa distribución hecha hace poco, xenon, automatico con levas al volante y 7 marchas. Navegador de serie con conexion por bluetoth y TV. Equipo de sonido de serie con subwoofer en bandeja. Asientos de cuero color beige. Control de crucero. Pantalla ordenador de abordo a color.", 5150, "https://img.milanuncios.com/fg/2626/21/262621972_3.jpg?VersionId=2WXcKInA5a6Lf2UVj_OUQwKnGi7gH1hn")
c10 = Coche(m4, "A6", 2004, 152000, "Diesel", 130, "Vehículo en muy buen estado. ITV al día. Equipado con extras como: elevalunas eléctricos, climatizador, 3 llaves, cierre centralizado con mando a distancia, sensor trasero de aparcamiento, airbag etc. Para más información no dude en contactar.", 3490, "https://cdn.wallapop.com/images/10420/94/3z/__/c10420p551100626/i1643420527.jpg?pictureSize=W640")
c11 = Coche(m3, "Serie 3", 1992, 235000, "Gasolina", 150, "Vehiculo nacional, primera matricula O-xxxx-BG 5/11/1992, 235.000km impecable estado, 2 juegos de llaves, todo original, itv recien pasada, todo al dia, aire acondicionado....todo funcionando perfectamente, mejor ver y probar.", 1500, "https://periodismodelmotor.com/wp-content/uploads/2016/01/curiosidades-bmw-m3-e36-1280x720.jpg")
c12 = Coche(m4, "A3", 2007, 278000, "Diesel", 110, "Motor 1.9 tdi 110cv- diésel precio al contado 4.500€ precio financiando con nosotros 4.200 euros 278.000km reales y certificados. garantía 12 meses ampliable a 24 con cobertura nacional y entrega a domicilio en toda españa. financia con nosotros desde 150€ al mes sin entrada. mantenimiento completo de los principales puntos de seguridad.", 4200, "https://cdn.wallapop.com/images/10420/5s/9v/__/c10420p349821156/i816465226.jpg?pictureSize=W640")
c13 = Coche(m6, "480 Turbo", 1991, 117000, "Gasolina", 120, "Coche en buen estado. Actualmente de baja temporal. Se entregaría rehabilitado sin ITV. Funcionando casi todo. Tiene algún fallo subsanable. Precio negociable. También aceptaría algún cambio por coche más moderno ajustando diferencia.", 1300, "https://img.milanuncios.com/fg/3287/21/328721514_3.jpg?VersionId=AQgNAbaCkhmGK5e5bMuPys8.y1BEPg0q")
c14 = Coche(m6, "S80", 2001, 257000, "Gasolina", 170, "Pongo a la venta Volvo s80 motor atmosférico 170cv 5 cilindros, caja de cambios automática, con bola de remolque homologada en la ficha técnica, el coche se encuentra en un estado muy bueno, era coche oficial del cuerpo diplomático hasta el año 2014 y después ha tenido un único dueño hasta hoy, al coche le funciona todo perfectamente y no tiene ni un solo fallo, el volante ni si quiera tiene ninguna marca de desgaste.", 2390, "https://img.clasf.es/2019/10/15/Volvo-S80-2002-20191015225055.3080860015.jpg")
c15 = Coche(m5, "19 Chamade", 1990, 180000, "Gasolina", 80, "Renault 19 Chamade modelo TSE, con 180.000 km. Motor 1.4 gasolina en perfecto estado, kit de distribución nuevo (bomba, correa y tensor), radiador con muy poco tiempo, electro auxiliar, al día de mantenimientos como filtros, aceite, valvulina, anticongelante... Ruedas nuevas, interiores en muy buen estado. Itv recién pasada el 27/12/2019.", 850, "https://www.donocasion.es/img/vehicles/000000295298.jpeg")
c16 = Coche(m5, "Clio", 2006, 225000, "Gasolina", 70, "", 1800, "Vehículo en muy buen estado con todo el mantenimiento recién hecho, elevalunas eléctricos, cierre centralizado, dirección asistida, aire acondicionado, radio cd, etc, transferido y con 12 meses de garantía")
c17 = Coche(m5, "R5", 1988, 175000, "Gasolina", 120, "Renault 5 GT Turbo a falta de restaurar ya que lleva tiempo parado, arranca bien, tiene correas y bombos de agua nueva, manguitos de silicona, homologado ancho de vías, asientos homologados, amortiguadores y muelles homologados, se entregan algunos recambios de origen.", 4900, "https://www.autofacil.es/elementosWeb/gestionCajas/AUF/Image/Trasera_1.jpg")
c18 = Coche(m7, "Land Cruiser", 2004, 259000, "Diesel", 163, "Toyota land cruiser 3.0 d-4d 163cv 4x4 automático con reductora, el más alto de su gama y en perfecto estado. Único propietario. historial de mantenimiento. kilómetros certificados. equipado con: dirección asistida, abs, esp, cierre centralizado, elevalunas eléctricos del. y tras., asientos calefactables con airbags e isofix, espejos abatibles y antideslumbrantes.", 12490, "https://e00-elmundo.uecdn.es/elmundomotor/imagenes/2004/02/23/1077536287_g.jpg")
c19 = Coche(m7, "Supra", 1988, 129000, "Gasolina", 238, "Toyota Supra, motor 3.0 6 cilindros TURBO 238CV, IMPECABLE, todo al dia, coche con muy poco uso, Solo dos dueños y los dos personas de adulta edad. Repasado de todo, gran historial en mantenimientos, y perfecto de chapa.", 11000, "https://img.milanuncios.com/fg/3393/33/339333835_4.jpg?VersionId=OwOeOu_Ub.HVQOzS2s33LXeSLvBm2I1U")
c20 = Coche(m7, "Prius", 2007, 150000, "Híbrido", 112, " Vehículo con distintivo ambiental eco en estado impecable equipado con los extras normales de este modelo", 6090, "https://www.km77.com/media/fotos/toyota_prius_2006_2093_2.jpg")

session.add(u1)
session.add(u2)

session.add(m1)
session.add(m2)
session.add(m3)
session.add(m4)
session.add(m5)
session.add(m6)
session.add(m7)

session.add(c1)
session.add(c2)
session.add(c3)
session.add(c4)
session.add(c5)
session.add(c6)
session.add(c7)
session.add(c8)
session.add(c9)
session.add(c10)
session.add(c11)
session.add(c12)
session.add(c13)
session.add(c14)
session.add(c15)
session.add(c16)
session.add(c17)
session.add(c18)
session.add(c19)
session.add(c20)

# # 10 - commit and close session
session.commit()
session.close()