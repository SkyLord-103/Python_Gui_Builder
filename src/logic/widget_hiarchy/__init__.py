from .parser import WidgetParser as _wp

from .widgets.widget_label import Label


def parse(**kw_props):
    """Parse key word arguments for properties"""
    return _wp(kw_props)
