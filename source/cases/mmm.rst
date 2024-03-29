:orphan:

Media Mix Models
================

.. grid:: 1 1 2 2

    .. grid-item::
        :columns: 12 12 5 5

        .. figure:: /images/cases/marketing.jpeg

    .. grid-item::
        :columns: 12 12 7 7

        Media Mix Models are analytical tools used to optimize marketing strategies by measuring the effectiveness of various marketing channels.
        They help in determining the best combination of channels to maximize ROI, drive customer engagement, and allocate budget effectively.
        Bayesian Inference offers several benefits in marketing analytics, particularly when assessing channel effectiveness:
        Bayesian models can incorporate prior knowledge and adapt to new data, making them suitable for analyzing complex and dynamic marketing environments.

MMM As a White Box
------------------

MMM is an actual :ref:`White-Box`. By accounting for uncertainty, Bayesian models provide more reliable and stable estimates, aiding in better-informed decision-making.
Bayesian models can handle sparse or small datasets, enabling accurate analysis even with limited data.
You can estimate individual channel impacts, allowing for tailored optimization of marketing efforts and budget allocation.
As new data becomes available, Bayesian models can be updated easily, allowing marketers to stay current with evolving trends and make timely adjustments to their strategies.


.. mermaid::

    flowchart LR
        brads{{Brand marketing spend}}
        pfads{{Performance marketing spend}}
        awe[Awareness]
        dem[Demand]
        int[Interest]
        con[Consideration]
        sal[Sales]
        pri{{Price}}
        comp_awe[Competition awareness]
        comp_int[Competition interest]
        comp_pri[Competition price]
        dem --> awe
        brads -.-> int
        brads -.-> awe
        comp_awe --> awe
        dem --> int
        awe --> int
        comp_int --> int
        pfads -.-> con
        int  --> con
        con --> sal
        pri -.-> sal
        pfads -.-> sal
        comp_pri --> sal
