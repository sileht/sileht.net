Title: About me
Slug: index

I'm Mehdi Abaakouk, I live in Toulouse (France) and I have been using
Linux for more than twenty years.

I co-founded and run [Mergify](https://mergify.io), a GitHub service around automation, and also setup and maintain the infrastructure of [tetaneutral.net](http://www.tetaneutral.net).

I worked as **Senior DevOps Engineer** and **Senior Software Engineer** for [Jolibrain](https://www.jolibrain.com/), [Wazo](https://wazo.io), [Qovery](https://www.qovery.com), [Red Hat](http://redhat.com/), [eNovance](https://www.redhat.com/en/about/press-releases/red-hat-acquire-enovance-leader-openstack-integration-services)
, [Capgemini](https://www.capgemini.com/), [DGAC](https://www.ecologique-solidaire.gouv.fr/en/french-civil-aviation-authority), [CNES](https://cnes.fr) and [GFI](https://gfi.world).

My main interests in computer science are **opensource software** and how
Internet works under the hood, and I **really** like to hack them.

Here is a quick list of my contribution to the opensource world:

-   The engine and website of [Mergify](https://github.com/Mergifyio/mergify-engine)
    <sup>Python, Redis, Postgresql, gunicorn, ReactJS, Nginx, Heroku, Sentry, Datadog</sup>
-   metadata extraction of the [Collectd](https://collectd.org) libvirt
    plugin <sup>C</sup>
-   [libvirt](https://libvirt.org) network interface statistics
    retrieval for openvswitch <sup>C</sup>
-   [neomutt](https://github.com/neomutt/neomutt), a text based mail
    client <sup>C</sup>
-   Core developer of [Gnocchi](https://gnocchi.xyz), Metric as a
    Service: multi-tenant timeseries, metrics and resources database
    <sup>Python, Ceph, Redis, Postgresql, Mysql</sup>
-   [CheckMK fastchecker](https://github.com/sileht/cmk_fastchecker)
    that removes overhead of loading python runtime on each CheckMK check run
    <sup>Python</sup>
-   [Openstack](http://www.openstack.org) where I am Core developer of
    the [Ceilometer](https://github.com/openstack/ceilometer),
    [Aodh](https://github.com/openstack/aodh),
    [Tooz](https://github.com/openstack/tooz),
    [Oslo.messaging](https://github.com/openstack/oslo.messaging) and
    all many other bricks of Openstack ecosystem <sup>Python, Mysql,
    Postgresql, Rabbitmq, Redis, Kafka</sup>
-   [Grafana Gnocchi datasource plugin](https://grafana.net/plugins/gnocchixyz-gnocchi-datasource)
    <sup>Javascript, Angular</sup>
-   [Pastamaker](https://github.com/sileht/pastamaker) a Github Gating
    Bot on top of Travis-CI, Github Pull Request and Github Branch
    protection system <sup>Python, Redis, Javascript, Angular, Heroku</sup>
-   A bunch of Python libraries:
    [git-pull-request](https://github.com/Merigfyio/git-pull-request),
    [daiquiri](https://github.com/jd/daiquiri),
    [cotyledon](https://github.com/sileht/cotyledon),
    [pifpaf](https://github.com/jd/pifpaf), ... <sup>Python, Cython</sup>
    [cradox](https://github.com/sileht/pycradox),
-   Ceph [librados](http://docs.ceph.com/docs/master/rados/api/python/)
    and
    [libcephfs](http://docs.ceph.com/docs/master/api/#ceph-filesystem-apis)
    Python binding in C with [Cython](http://cython.org) <sup>C, Cython</sup>
-   Official Red Hat Openstack Packaging <sup>.rpm Packaging</sup>
-   [Official Debian Packaging](http://qa.debian.org/developer.php?login=sileht%40sileht.net)
    <sup>.deb packaging</sup>
-   [Disc-air](https://chiliproject.tetaneutral.net/projects/git-tetaneutral-net/repository/disc-air)
    a tools to graph a L2 network (started 2015) <sup>Python</sup>
-   [Neutron routed-plugin](https://chiliproject.tetaneutral.net/projects/git-tetaneutral-net/repository/neutron-linuxrouted-plugin)
    OpenStack plugin to provide L3 routing only <sup>Python</sup>
-   [Bird-LG](https://github.com/sileht/bird-lg/) a BGP looking glass
    for bird written in python/flask
    <sup>Python/JQuery</sup>
-   [Listen](https://launchpad.net/listen) a music player/manager for
    GNOME written in python/gtk/gstreamer (2005-2012)
    <sup>Python/GTK/Gstreamer</sup>
-   [Seeks](https://github.com/beniz/seeks) a social and collaborative
    search engine , I make the debian and ubuntu packages (2009-2012)
    <sup>C++</sup>
-   [Lullaby](https://github.com/sileht/lullaby) a android client for
    [ampache](http://ampache.org/) (2010-2012) <sup>Java/Android</sup>
-   [CyanogenMod/Lineageos](https://lineageos.org) a Android alternative OS
    for mobile, I have ported some CyanogenMod fonctionnalities from
    version 4 to 5, 6 and 7 (2009-2010)
    <sup>C/Linux kernel/Java/Android</sup>
-   [Gmixer](http://launchpad.net/gmixer) a audio mixer in
    python/gtk (2008) <sup>Python</sup>

For the Internet part, I'm involved in a French Associative
Internet Service Provider and Host Provider:
[tetaneutral.net](http://www.tetaneutral.net)

In this context, since 2010, I have set up and maintained:

-   an [OpenStack](http://www.openstack.org) cluster of 14 nodes using
    [Kvm](http://www.linux-kvm.org) for the virtualisation (~180
    instances), [Ceph](http://ceph.com/) for the storage (~100To), and
    a [custom network
    plugins](https://chiliproject.tetaneutral.net/projects/git-tetaneutral-net/repository/neutron-linuxrouted-plugin)
    that uses iBGP mesh network to route public ips across the cluster
    with [Bird](https://bird.network.cz/).
-   that has replaced an old cluster of 6 nodes built with
    [ganeti](http://code.google.com/p/ganeti/).
-   a mailserver system with 3
    [HA/replicated](http://wiki.dovecot.org/Replication) nodes using
    [Dovecot](http://www.dovecot.org/) and
    [Postfix](http://www.postfix.org/)
-   an infrastructure supervision with
    [CheckMK](http://http://mathias-kettner.de/check_mk.html) and
    [cmk\_fastchecker](https://github.com/sileht/cmk_fastchecker)
-   an monitoring platform using [Prometheus](https://prometheus.io) and
    [Grafana](https://grafana.com)
-   some tools like [Bird-LG](https://github.com/sileht/bird-lg/) for
    our [looking glass](http://lg.tetaneutral.net/)
-   or
    [disc-air](https://chiliproject.tetaneutral.net/projects/git-tetaneutral-net/repository/disc-air)
    to [map our network](https://tsf.tetaneutral.net/)
-   and everything automated with [Puppet](https://puppetlabs.com/)
    and/or [Ansible](https://ansible.com)
-   and backuped with [Borg](http://borgbackup.readthedocs.org)

I'm taking charge if the regular system administration tasks too.

And also I like to dance on crazy swing rhythm 😁
