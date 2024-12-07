from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Service, Washer, Box, CarWashBooking, Client


def book_service(request):
    """Запись клиента на услугу с учетом проверки занятости мест в боксе."""
    services = Service.objects.all()
    washers = Washer.objects.all()
    boxes = Box.objects.all()
    clients = Client.objects.all()

    if request.method == 'POST':
        # Получение данных из формы
        client_id = request.POST.get('client_id')
        if not client_id or not Client.objects.filter(id=client_id).exists():
            messages.error(request, 'Неверный идентификатор клиента.')
            return redirect('book_service')

        service_id = request.POST.get('service_id')
        if not service_id or not Service.objects.filter(id=service_id).exists():
            messages.error(request, 'Неверный идентификатор услуги.')
            return redirect('book_service')

        washer_id = request.POST.get('washer_id')
        if not washer_id or not Washer.objects.filter(id=washer_id).exists():
            messages.error(request, 'Неверный идентификатор мойщика.')
            return redirect('book_service')

        box_id = request.POST.get('box_id')
        if not box_id or not Box.objects.filter(id=box_id).exists():
            messages.error(request, 'Неверный идентификатор бокса.')
            return redirect('book_service')
        booking_time = timezone.datetime.fromisoformat(request.POST['booking_time'])

        # Получаем данные о сервисе
        service = get_object_or_404(Service, id=service_id)
        duration = timedelta(minutes=service.duration)
        end_time = booking_time + duration

        # Проверка занятости мест
        box = get_object_or_404(Box, id=box_id)
        if CarWashBooking.objects.filter(
            box=box,
            booking_time__lt=end_time,
            booking_time__gte=booking_time
        ).count() >= box.available_spots:
            messages.error(request, 'Все места в этом боксе заняты на выбранное время.')
            return render(request, 'wash/book_service.html', {
                'services': services,
                'washers': washers,
                'boxes': boxes,
                'clients': clients,
                'current_time': timezone.now().isoformat(),
            })

        # Проверка занятости мойщика
        if CarWashBooking.objects.filter(
            washer_id=washer_id,
            booking_time__lt=end_time,
            booking_time__gte=booking_time
        ).exists():
            messages.error(request, 'Этот мойщик уже занят в выбранное время.')
            return render(request, 'wash/book_service.html', {
                'services': services,
                'washers': washers,
                'boxes': boxes,
                'clients': clients,
                'current_time': timezone.now().isoformat(),
            })

        # Создание записи
        client = get_object_or_404(Client, id=client_id)
        washer = get_object_or_404(Washer, id=washer_id)
        CarWashBooking.objects.create(
            client=client,
            service=service,
            washer=washer,
            box=box,
            booking_time=booking_time
        )

        messages.success(request, 'Клиент успешно записан!')
        return render(request, 'wash/book_service.html', {
            'services': services,
            'washers': washers,
            'boxes': boxes,
            'clients': clients,
            'current_time': timezone.now().isoformat(),
        })

    return render(request, 'wash/book_service.html', {
        'services': services,
        'washers': washers,
        'boxes': boxes,
        'clients': clients,
        'current_time': timezone.now().isoformat(),
    })


def schedule(request):
    """Просмотр расписания записей, отсортированных по времени."""
    bookings = CarWashBooking.objects.select_related('client', 'service', 'washer', 'box').order_by('booking_time')
    return render(request, 'wash/schedule.html', {'bookings': bookings})