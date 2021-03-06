from __future__ import unicode_literals
from .job import updateJobsnr, updateJobsDefinednr
from .client import updateClientsDefinednr
from .storage import updateStorageDefinednr, updateStorageVolumesnr, updateStoragedetectdedup
from .task import updateTasksrunningall
from .user import updateUsersnr
from .department import updateDepartmentsnr
from .role import updateRolesnr
from .vmhosts import updateVMhostsdetectvsphere, updateClientsVMnrlist
from .ibadmin import IBADVERSION


def updateMenuNumbers(request, context):
    updateJobsnr(request, context)
    updateJobsDefinednr(request, context)
    updateClientsDefinednr(request, context)
    updateStorageDefinednr(request, context)
    updateStorageVolumesnr(request, context)
    updateStoragedetectdedup(request, context)
    updateVMhostsdetectvsphere(request, context)
    updateTasksrunningall(request, context)
    updateClientsVMnrlist(request, context)
    updateUsersnr(request, context)
    updateRolesnr(request, context)
    updateDepartmentsnr(request, context)
    context['ibadminver'] = IBADVERSION

