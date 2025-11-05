from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.upgrade_button = page.get_by_role("button", name="Upgrade")
        self.performance_button = page.get_by_role("link", name="Performance")
        self.dashboard_button = page.get_by_role("link", name="Dashboard")
                

    def is_upgrade_button_visible(self):
        upgrade_button = self.upgrade_button
        return upgrade_button.is_visible()

    def is_performance_button_visible(self):
        performance_button = self.performance_button
        return performance_button.is_visible()

    def is_dashboard_button_visible(self):
        dashboard_button = self.dashboard_button
        return dashboard_button.is_visible()
    
    def click_performance(self):
        performance_button = self.performance_button
        performance_button.click()
        
    def click_dashboard(self):
        dashboard_button = self.dashboard_button
        dashboard_button.click()
        
    def click_upgrade(self):
        upgrade_button = self.upgrade_button
        upgrade_button.click()
    
    
    
    