from utils.basepath_helper import utils_path
class HTML5:
    JQUERY_URL = "http://code.jquery.com/jquery-1.11.2.min.js"
    JQUERY_LOAD_HELPER = "jquery_load_helper.js"
    DRAG_AND_DROP_HELPER = utils_path + "drag_and_drop_helper.js"

    @staticmethod
    def __load_jquery(driver, jquery_url=JQUERY_URL):
        with open(HTML5.JQUERY_LOAD_HELPER) as f:
            load_jquery_js = f.read()

        #print("JQuery JS:", load_jquery_js)
        driver.execute_async_script(load_jquery_js, jquery_url)

    @staticmethod
    def drag_and_drop(driver, draggable, droppable):
        HTML5.__load_jquery(driver)
        with  open(HTML5.DRAG_AND_DROP_HELPER) as f:
            drag_and_drop_js = f.read()

        #print("Drag and Drop JS:", drag_and_drop_js)
        drag_and_drop_command = "$('{draggable}').simulateDragDrop({{ dropTarget: '{droppable}'}});"\
            .format(draggable=draggable, droppable=droppable)
        print("Drag and Drop Command:", drag_and_drop_command)
        driver.execute_script(drag_and_drop_js + drag_and_drop_command)