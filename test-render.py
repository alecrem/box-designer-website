import boxmaker, logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.info("---------------------------------------------------------------------------")

#boxmaker.render("tmp/test.pdf",101.6,127.00001,152.4,4.7625,0.0,11.90625,True)
# boxmaker.render("tmp/test.pdf",95.25,76.2,76.2,3.048,0.0,7.62,True)
boxmaker.render("tmp/boxes/drawers.pdf",90,70,50,3,0.0,8,False,'pdf',True,3)
boxmaker.render("tmp/boxes/tray.pdf",90,70,50,3,0.0,8,False,'pdf',True)

# python test-render.py&&open tmp/boxes/tray.pdf&&open tmp/boxes/drawers.pdf