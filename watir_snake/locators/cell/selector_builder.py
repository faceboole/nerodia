import logging

from ..element.selector_builder import SelectorBuilder as ElementSelectorBuilder


class SelectorBuilder(ElementSelectorBuilder):
    def _build_wd_selector(self, selectors):
        if any(isinstance(selector, re._pattern_type) for selector in selectors):
            return None

        expressions = ['./th', './td']
        attr_expr = self.xpath_builder.attribute_expression(None, selectors)

        if attr_expr:
            expressions = ['{}[{}]'.format(e, attr_expr) for e in expressions]

        xpath = " | ".join(expressions)

        logging.debug({'build_wd_selector': xpath})

        return ['xpath', xpath]
