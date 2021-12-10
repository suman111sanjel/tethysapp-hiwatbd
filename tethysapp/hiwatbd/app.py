from tethys_sdk.base import TethysAppBase, url_map_maker


class Hiwatbd(TethysAppBase):
    """
    Tethys app class for Hiwatbd.
    """

    name = 'HIWAT Extreme - Bangladesh'
    index = 'hiwatbd:home'
    icon = 'hiwatbd/images/icon.gif'
    package = 'hiwatbd'
    root_url = 'hiwatbd'
    color = '#2c3e50'
    description = ''
    tags = 'HIWAT'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='hiwatbd',
                controller='hiwatbd.controllers.home'
            ), UrlMap(
                name='getLatestHIWATInfo',
                url='hiwatbd/getLatestHIWATInfo',
                controller='hiwatbd.controllers.getLatestHIWATInfo'
            ),
        )

        return url_maps

