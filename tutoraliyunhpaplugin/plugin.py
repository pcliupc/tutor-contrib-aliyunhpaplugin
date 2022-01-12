from glob import glob
import os
import pkg_resources

from .__about__ import __version__

templates = pkg_resources.resource_filename(
    "tutoraliyunhpaplugin", "templates"
)

config = {
    "defaults": {
        "HPA_CPU_UTILIZATION": 60,
        "HPA_MEM_UTILIZATION": 80,

        "HPA_LMS_MIN_REPLICAS": 2,
        "HPA_LMS_MAX_REPLICAS": 32,
        "ELASTICWORKLOAD_SOURCE_LMS_MIN_REPLICAS": 2,
        "ELASTICWORKLOAD_SOURCE_LMS_MAX_REPLICAS": 2,
        "ELASTICWORKLOAD_VK_LMS_MIN_REPLICAS": 0,
        "ELASTICWORKLOAD_VK_LMS_MAX_REPLICAS": 32,

        "HPA_CMS_MIN_REPLICAS": 2,
        "HPA_CMS_MAX_REPLICAS": 16,
        "ELASTICWORKLOAD_SOURCE_CMS_MIN_REPLICAS": 2,
        "ELASTICWORKLOAD_SOURCE_CMS_MAX_REPLICAS": 2,
        "ELASTICWORKLOAD_VK_CMS_MIN_REPLICAS": 0,
        "ELASTICWORKLOAD_VK_CMS_MAX_REPLICAS": 16,

        "HPA_LMS_WORKER_MIN_REPLICAS": 1,
        "HPA_LMS_WORKER_MAX_REPLICAS": 16,
        "ELASTICWORKLOAD_SOURCE_LMS_WORKER_MIN_REPLICAS": 1,
        "ELASTICWORKLOAD_SOURCE_LMS_WORKER_MAX_REPLICAS": 2,
        "ELASTICWORKLOAD_VK_LMS_WORKER_MIN_REPLICAS": 0,
        "ELASTICWORKLOAD_VK_LMS_WORKER_MAX_REPLICAS": 32,

        "HPA_CMS_WORKER_MIN_REPLICAS": 1,
        "HPA_CMS_WORKER_MAX_REPLICAS": 16,
        "ELASTICWORKLOAD_SOURCE_CMS_WORKER_MIN_REPLICAS": 1,
        "ELASTICWORKLOAD_SOURCE_CMS_WORKER_MAX_REPLICAS": 2,
        "ELASTICWORKLOAD_VK_CMS_WORKER_MIN_REPLICAS": 0,
        "ELASTICWORKLOAD_VK_CMS_WORKER_MAX_REPLICAS": 16,

        "HPA_FORUM_MIN_REPLICAS": 2,
        "HPA_FORUM_MAX_REPLICAS": 32,
        "ELASTICWORKLOAD_SOURCE_FORUM_MIN_REPLICAS": 2,
        "ELASTICWORKLOAD_SOURCE_FORUM_MAX_REPLICAS": 2,
        "ELASTICWORKLOAD_VK_FORUM_MIN_REPLICAS": 0,
        "ELASTICWORKLOAD_VK_FORUM_MAX_REPLICAS": 32,
    }
}

hooks = {}


def patches():
    all_patches = {}
    patches_dir = pkg_resources.resource_filename(
        "tutoraliyunhpaplugin", "patches"
    )
    for path in glob(os.path.join(patches_dir, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
