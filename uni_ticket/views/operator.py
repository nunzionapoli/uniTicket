from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import gettext as _

from organizational_area.models import *

from uni_ticket.decorators import is_operator
from uni_ticket.models import *
from uni_ticket.settings import OPERATOR_PREFIX
from uni_ticket.utils import user_offices_list, visible_tickets_to_user


@login_required
@is_operator
def dashboard(request, structure_slug, structure, office_employee):
    """
    Operator Dashboard

    :type structure_slug: String
    :type structure: OrganizationalStructure (from @is_operator)
    :type office_employee: OrganizationalStructureOfficeEmployee (from @is_operator)

    :param structure_slug: structure slug
    :param structure: structure object (from @is_operator)
    :param office_employee: employe offices queryset (from @is_operator)

    :return: render
    """
    title = _("Pannello di Controllo")
    sub_title = _("Gestisci le richieste in modalità {}").format(
        OPERATOR_PREFIX)
    template = "operator/dashboard.html"
    offices = user_offices_list(office_employee)
    user_tickets = visible_tickets_to_user(
        user=request.user, structure=structure, office_employee=office_employee
    )
    tickets = Ticket.objects.filter(code__in=user_tickets)
    not_closed = tickets.filter(is_closed=False)
    # unassigned = []
    # opened = []
    # my_opened = []
    unassigned = 0
    opened = 0
    my_opened = 0
    for nc in not_closed:
        if nc.has_been_taken():
            # opened.append(nc)
            opened += 1
            if nc.has_been_taken_by_user(structure=structure, user=request.user):
                # my_opened.append(nc)
                my_opened += 1
        else:
            # unassigned.append(nc)
            unassigned += 1
    # chiusi = tickets.filter(is_closed=True)
    chiusi = tickets.filter(is_closed=True).count()

    messages = TicketReply.get_unread_messages_count(tickets=tickets)

    d = {
        "offices": offices,
        "structure": structure,
        "sub_title": sub_title,
        "title": title,
        "ticket_aperti": opened,
        "ticket_assegnati_a_me": my_opened,
        "ticket_chiusi": chiusi,
        "ticket_messages": messages,
        "ticket_non_gestiti": unassigned,
    }
    return render(request, template, d)
