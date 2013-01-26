from plone.app.users.browser.personalpreferences import UserDataPanelAdapter

class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    def get_isVisibleFor(self):
        return self.context.getProperty('isVisibleFor', '')
    def set_isVisibleFor(self, value):
        return self.context.setMemberProperties({'isVisibleFor': value})
    isVisibleFor = property(get_isVisibleFor, set_isVisibleFor)