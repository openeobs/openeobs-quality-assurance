"""
    helpers on graphs in patient page
"""
from openeobs_mobile.page_helpers import BasePage
from openeobs_mobile.patient_page_locators import RANGIFY_CONTROL, \
    CHART_CONTEXT_GRAPH, CHART_FOCUS_GRAPHS, CHART_GRAPH_LABEL, \
    CHART_GRAPH_MEASUREMENT, GRAPH_TAB_BUTTON
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class PatientPageGraphs(BasePage):
    """
    helpers on graphs in patient page
    """

    def rangify_control_is_shown(self):
        """
        Check that the rangify control is shown
        :return: Boolean of if the rangify control is shown
        """
        try:
            self.driver.find_element(
                *RANGIFY_CONTROL
            )
        except NoSuchElementException:
            return False
        return True

    def get_context_graph(self):
        """
        Get the context graph element
        :return: The WebElement of the context graph
        """
        return self.driver.find_element(
            *CHART_CONTEXT_GRAPH
        )

    def get_focus_graphs(self):
        """
        Get the focus graphs of the obs chart
        :return: A list of focus graph WebElements
        """
        return self.driver.find_elements(
            *CHART_FOCUS_GRAPHS
        )

    @staticmethod
    def get_graph_label(graph):
        """
        Get the label for a graph WebElement
        :param graph: The graph WebElement to do operation on
        :return: Label as text
        """
        label = graph.find_element(
            *CHART_GRAPH_LABEL
        )
        return label.text

    @staticmethod
    def get_graph_measurement(graph):
        """
        Get the measurement for a graph WebElement
        :param graph: The graph WebElement to do operation on
        :return: Label as text
        """
        measurement = graph.find_element(
            *CHART_GRAPH_MEASUREMENT
        )
        return measurement.text

    @staticmethod
    def get_graph_measurements(graph):
        """
        Get the measurements (as in multiple) for a graph WebElement
        :param graph: The graph WebElement to do operation on
        :return: Label as text
        """
        measurements = graph.find_elements(
            *CHART_GRAPH_MEASUREMENT
        )
        return measurements

    def change_to_chart(self):
        """
        Change the tabs so shows the chart
        """
        tab = self.driver.find_element(
            *GRAPH_TAB_BUTTON
        )
        tab.click()
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR,
                                              '#graph-content #chart svg'))
        )

