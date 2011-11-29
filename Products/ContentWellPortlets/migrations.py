import logging

def from_2_1_to_3(context):
    context.runImportStepFromProfile('profile-Products.ContentWellPortlets:default',
            'viewlets')
    context.runImportStepFromProfile('profile-Products.ContentWellPortlets:default',
            'portlets')
    log = logging.getLogger("ContentWellPortlets")
    log.info("Ran viewlets and portlets import steps")
    
